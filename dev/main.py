from asyncio import sleep as async_sleep
from asyncio import run as async_run
from asyncio import CancelledError
from console_logger import log
from config_loader import load_config
from connection_checker import waiting_internet_connection

config = ""

async def main_loop():
    try:
        log("!!! SERVICE STARTED !!!")
        log("Loading configuration...")
        config = load_config()
        log("Config done")
        while True:
            waiting_network_connection()
            return False
    except Exception as e:
        log(f"Main script crush:{e}")
    finally:
        log("!!! SERVICE TERMINATED !!!")

def main():
    async_run(main_loop())

if __name__ == "__main__":
    main()
