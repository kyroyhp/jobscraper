from socket import create_connection
from time import sleep
from console_logger import log

network_status = None

def check_connection(host="8.8.8.8", port=443, timeout=3):
    try:
        with create_connection((host, port), timeout=timeout):
            return True
    except OSError:
        return False

def waiting_network_connection(config):
    global network_status
    while True:
        connected = check_connection()
        if connected:
            if network_status is False:
                log("Internet connection restored!")
            network_status = True
            return True
        if network_status is not False:
            log("Internet connection lost!")
        network_status = False
        log("Waiting internet connection...")
        log(f"Retry after {config['network']['check_interval']} seconds...")
        sleep(check_interval)
