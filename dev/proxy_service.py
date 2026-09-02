from time import sleep
from requests import get as request_get
from requests.exceptions import RequestException
from bs4 import BeautifulSoup
from console_logger import log
from connection_checker import waiting_network_connection
def get_proxy_list(config):
    while True:
        waiting_network_connection(config)
        try:
            url = "https://free-proxy-list.net/"
            response = request_get(
                url,
                timeout=15
            )
            response.raise_for_status()
            soup = BeautifulSoup(
                response.text,
                "html.parser"
            )
            table = soup.find(
                "table",
                {
                    "class":
                    "table table-striped table-bordered"
                }
            )
            proxy_list = []
            for row in table.find_all("tr")[1:]:
                columns = row.find_all("td")
                if columns:
                    ip = columns[0].text.strip()
                    port = columns[1].text.strip()
                    proxy_list.append(f"{ip}:{port}")
            if proxy_list:
                return proxy_list
            log("Proxy list empty. Retry...")
        except RequestException as e:
            log(f"Proxy download error: {e}")
        sleep(config["proxy"]["timeout"])
