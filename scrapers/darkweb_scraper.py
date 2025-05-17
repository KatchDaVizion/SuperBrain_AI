# SuperBrain AI Platform
# Created by David Louis-Charles (GitHub: KatchDaVizion)
# © 2025 All Rights Reserved — https://github.com/KatchDaVizion

import requests
from stem import Signal
from stem.control import Controller
from bs4 import BeautifulSoup

def rotate_tor_ip():
    with Controller.from_port(port=9051) as controller:
        controller.authenticate(password="mytorpass")
        controller.signal(Signal.NEWNYM)

def scrape_onion(onion_url):
    session = requests.Session()
    session.proxies = {
        'http': 'socks5h://127.0.0.1:9050',
        'https': 'socks5h://127.0.0.1:9050'
    }
    res = session.get(onion_url)
    soup = BeautifulSoup(res.text, 'html.parser')
    return soup.get_text()


__author_id__ = "KatchDaVizion_2025_DLC_SIG"

def check_license():
    allowed_user = "David Louis-Charles"
    return allowed_user in __author_id__
