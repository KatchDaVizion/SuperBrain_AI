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

    # ✅ Create file if missing
    if not os.path.exists(path):
        print(f"[🗝️] '{file}' not found. Let's create it.")
        key = input(f"{hint}\nEnter your API key for {file}: ").strip()
        if key:
            save_key(file, key)
        else:
            log_warning(f"No key entered for {file}. Skipping.", module="config")
        return key

    # ✅ Read existing key
    with open(path) as f:
        key = f.read().strip()

    # 🔁 If key is empty, ask again
    if not key:
        print(f"[⚠️] '{file}' is empty. Please provide a valid key.")
        key = input(f"{hint}\nEnter your API key for {file}: ").strip()
        if key:
            save_key(file, key)
        else:
            log_warning(f"No key entered for {file}. Skipping.", module="config")
        return key

    # ✅ Optionally check if API key works
    if api_check:
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

            # Optional: custom logic
            if api_check.get('response_check'):
                if not api_check['response_check'](response.json()):
                    log_warning(f"{file} API key failed check. Re-prompting...", module="config")
                    os.remove(path)
                    return load_key(file, hint, api_check)

            log_info(f"{file} API key validated.", module="config")

        except requests.exceptions.HTTPError as e:
            if e.response.status_code in [401, 403]:
                log_warning(f"{file} API key unauthorized. Re-prompting...", module="config")
                os.remove(path)
                return load_key(file, hint, api_check)
            else:
                log_error(f"HTTP error during API key check: {e}", module="config")
        except requests.exceptions.RequestException as e:
            log_error(f"Network error during API key check: {e}", module="config")

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
