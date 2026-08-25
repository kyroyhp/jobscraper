from socket import create_connection
from time import sleep
from console_logger import log

network_status = True

def check_connection(host="8.8.8.8", port=443, timeout=3):
    try:
        with create_connection((host, port), timeout=timeout):
            return True
    except OSError:
        return False

def waiting_internet_connection(check_interval=10):
    global network_status

    if check_connection():
        if not network_status:
            log("Internet connection restored!")
        network_status = True
        return

    if network_status:
        log("Internet connection lost!")
        network_status = False

    while not check_connection():
        log("Waiting internet connection...")
        log(f"Retry connection after {check_interval} seconds...")
        sleep(check_interval)

    log("Internet connection restored!")
    network_status = True
