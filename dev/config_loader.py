import sys
from yaml import safe_load
from os.path import dirname, abspath, join, exists
from console_logger import log

DEFAULT_CONFIG_FILE_NAME = "config.yaml"
DEFAULT_CONFIG = """
service:
  interval: 300

network:
  check_interval: 10

proxy:
  enabled: true
  retries: 5
  timeout: 10

scraper:
  timeout: 20
"""

def get_app_dir():
    if getattr(sys, 'frozen', False):
        return dirname(sys.executable)
    return dirname(abspath(__file__))

def get_config_path():
    return join(get_app_dir(), DEFAULT_CONFIG_FILE_NAME)

def create_default_config(path):
    try:
        log("Creating default config...")
        with open(path, "w", encoding="utf-8") as f:
            f.write(DEFAULT_CONFIG)
        log("Config created.")
        input("Edit 'config.yaml' and press Enter...")
    except Exception as e:
        log(f"Config creation error: {e}")
        raise

def validate_config(cfg):
    errors = []
    if "service" not in cfg:
        errors.append("Missing service section")
    if "network" not in cfg:
        errors.append("Missing network section")
    if "proxy" not in cfg:
        errors.append("Missing proxy section")
    if "scraper" not in cfg:
        errors.append("Missing scraper section")
    if errors:
        raise ValueError(
            "\n".join(errors))
    return True

def load_config():
    path = get_config_path()
    if not exists(path):
        log("Config file not found")
        create_default_config(path)
    try:
        with open(path, "r", encoding="utf-8") as f:
            cfg = safe_load(f)
        if not isinstance(cfg, dict):
            raise ValueError("Config must be YAML dictionary")
        validate_config(cfg)
        return cfg
    except Exception as e:
        log("Can't load configuration")
        raise
