from asyncio import sleep as async_sleep
from asyncio import run as async_run
from asyncio import CancelledError
from console_logger import log
from config_loader import load_config
from connection_checker import waiting_network_connection
from proxy_service import get_proxy_list
# from jobs_scraper import search_jobs

async def main_loop():
    try:
        log("!!! SERVICE STARTED !!!")
        log("Loading configuration...")
        config = load_config()
        log("Config done")
        while True:
            waiting_network_connection(config)
            log("Loading proxies...")
            proxy_list = get_proxy_list(config)
            log(f"Loaded proxies: {len(proxy_list)}")
            print(proxy_list)
            log("Searching jobs...")
           # jobs = search_jobs(config, proxy_list)
           # log(f"Found jobs: {len(jobs)}")
            await async_sleep(config["service"]["interval"])

    except CancelledError:
        log("Service cancelled")
    except Exception as e:
        log(f"Main script crashed: {e}")
    finally:
        log("!!! SERVICE TERMINATED !!!")

def main():
    async_run(main_loop())

if __name__ == "__main__":
    main()
