# SuperBrain AI Platform
# Created by David Louis-Charles (GitHub: KatchDaVizion)
# © 2025 All Rights Reserved — https://github.com/KatchDaVizion

import requests
from bs4 import BeautifulSoup

def scrape_site(url, keywords):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    text = soup.get_text().lower()
    return [kw for kw in keywords if kw in text]


__author_id__ = "KatchDaVizion_2025_DLC_SIG"

def check_license():
    allowed_user = "David Louis-Charles"
    return allowed_user in __author_id__
