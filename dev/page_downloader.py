import random
from time import sleep
from requests import get as request_get
from requests.exceptions import RequestException
from console_logger import log
USER_AGENT = (
    "Mozilla/5.0 "
    "(Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 "
    "Chrome/140 Safari/537.36"
)
def download_page(url, config, proxy_list):
    attempts = config["proxy"]["retries"]
    for attempt in range(attempts):
        if not proxy_list:
            log("Proxy list empty")
            return None
        proxy = random.choice(proxy_list)
        proxies = {
            "http": f"http://{proxy}"
        }
        headers = {"User-Agent": USER_AGENT}
        try:
            log(
                f"Trying proxy {proxy} "
                f"({attempt + 1}/{attempts})"
            )
            response = request_get(
                url,
                headers=headers,
                proxies=proxies,
                timeout=config["scraper"]["timeout"]
            )
            response.raise_for_status()
            return response.text
        except RequestException as e:
            log(f"Proxy failed {proxy}: {e}")
            if proxy in proxy_list:
                proxy_list.remove(proxy)
            sleep(1)
    log("All proxy attempts failed")
    return None
