import sys
from yaml import safe_load, dump
from os.path import dirname, abspath, join, exists
from console_logger import log

CONFIG_FILE_NAME = "config.yaml"

# get application directory
def get_app_dir():
    if getattr(sys, 'frozen', False):
        return dirname(sys.executable)
    return dirname(abspath(__file__))

def get_config_path():
    return join(get_app_dir(), CONFIG_FILE_NAME)

def create_default_config(path):
    try:
        log("Creating a default config file...")
        with open(path, "w", encoding="utf-8") as f:
            f.write(DEFAULT_CONFIG_FILE)
        log("Please open the 'config.yaml' and fill in the required fields.")
        input("Press 'Enter' after editing the config file")
    except Exception as e:
        log(f"An error occurred while creating a config file: {e}")

def load_config():
    path = get_config_path()
    if not exist(path):
        log("'config.yaml' not found.")
        create_default_config(path)

    with open(path, "r" encoding="utf-8") as f:
        return safe_load(f)

def validate_config(cfg):
    errors = []
    
     # TELEGRAM
    if cfg["USE_TELEGRAM_BOT"]:
        if not cfg["TOKEN"]:
            errors.append("'TOKEN' was empty")
        if not cfg["CHANNEL_ID"]:
            errors.append("'CHANNEL_ID' was empty")

        if cfg["FRAGMENT_SIZE"] < 1 or cfg["FRAGMENT_SIZE"] > 20:
            errors.append("'FRAGMENT_SIZE' must be between 1...20")

        if cfg["POSTING_DELAY"] < 60:
            errors.append("'POSTING_DELAY' must be >=60")
