# SuperBrain AI Platform
# Created by David Louis-Charles (GitHub: KatchDaVizion)
# © 2025 All Rights Reserved — https://github.com/KatchDaVizion

# utils/config.py
import os
import json
import time
import requests
from utils.logger import log_info, log_warning, log_error

CONFIG_DIR = "../configs"
os.makedirs(CONFIG_DIR, exist_ok=True)

def load_key(file, hint, api_check=None):
    path = os.path.join(CONFIG_DIR, file)
    key = None
    if os.path.exists(path):
        with open(path) as f:
            key = f.read().strip()

    if not key:
        log_warning(f"Missing or invalid {file}. {hint}", module="config")
        key = input(f"Enter API key for {file} (or leave blank to skip): ").strip()
        if key:
            save_key(file, key)
        return key

    if api_check:
        if not api_check['url']:
            log_warning(f"API check URL not provided for {file}.", module="config")
            return key
        try:
            headers = api_check.get('headers', {})
            method = api_check.get('method', 'get').lower()
            data = api_check.get('data')

            response = None
            if method == 'post':
                response = requests.post(api_check['url'], headers=headers, json=data)
            else:
                response = requests.get(api_check['url'], headers=headers)

            response.raise_for_status()
            if api_check.get('response_check'):
                if not api_check['response_check'](response.json()):
                    log_warning(f"Stored API key for {file} seems invalid.", module="config")
                    os.remove(path)
                    return load_key(file, hint, api_check)
            elif response.status_code in [401, 403]:
                log_warning(f"Stored API key for {file} is unauthorized.", module="config")
                os.remove(path)
                return load_key(file, hint, api_check)
            else:
                log_info(f"API key for {file} checked and seems valid.", module="config")

        except requests.exceptions.RequestException as e:
            log_error(f"Error checking API key for {file}: {e}", module="config")
            # Don't invalidate on network errors

    return key

def save_key(file, key):
    path = os.path.join(CONFIG_DIR, file)
    with open(path, 'w') as f:
        f.write(key)
    log_info(f"API key saved to {path}", module="config")


__author_id__ = "KatchDaVizion_2025_DLC_SIG"

def check_license():
    allowed_user = "David Louis-Charles"
    return allowed_user in __author_id__
