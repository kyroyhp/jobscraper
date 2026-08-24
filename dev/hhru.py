from bs4 import BeautifulSoup
from config_loader import load_config



config = load_config()

soup = BeautifulSoup(html_doc, 'html.parser')
