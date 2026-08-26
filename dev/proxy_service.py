import random
from time import sleep
from requests import get as request_get
from requests.exceptions import RequestException
from bs4 import BeautifulSoup
from config_loader import load_config
from console_logger import log
from connection_checker import waiting_network_connection

def get_proxy_list(config):
    while True:
        waiting_network_connection(config)

        try:
            url = 'https://free-proxy-list.net/'
            response = request_get(url, timeout=15)
            response.raise_for_status()

            soup = BeautifulSoup(response.text, 'html.parser')
            table = soup.find('table', {'class': 'table table-striped table-bordered'})

            proxies = []
            for row in table.find_all('tr')[1:]:
                columns = row.find_all('td')
                if columns:
                    ip = columns[0].text.strip()
                    port = columns[1].text.strip()
                    proxies.append(f"http://{ip}:{port}")

            if proxies:
                return proxies

            log(f"The proxy list is empty. Retry after {config['proxy']['timeout']} seconds...")
            sleep(config['proxy']['timeout'])

        except RequestException as e:
            log(f"Error fetching proxy list: {e}")
            sleep(config['proxy']['timeout'])

def retry_request(url, params=None):
    while True:
        waiting_internet_connection(config)

        proxies = find_proxies()
        for attempt in range(1, config['proxy']['retries'] + 1):
            proxy = {'http': random.choice(proxies)}
            try:
                response = request_get(
                    url,
                    params=params,
                    proxies=proxy,
                    timeout=20
                )
                response.raise_for_status()
                return response
            except RequestException as e:
                log(f"Attempt {attempt}/{config['proxy']['retries']} connection with proxy failed: {e}")
                sleep(config['network']['timeout']/2)

        log(f"All attempts failed. Retry after {config['proxy']['timeout']} seconds...")
        sleep(config['proxy']['timeout'])
