# SuperBrain AI Platform
# Created by David Louis-Charles (GitHub: KatchDaVizion)
# © 2025 All Rights Reserved — https://github.com/KatchDaVizion

# utils/memory.py
import json
import os
from datetime import datetime

MEMORY_FILE = "memory_db.json"

def load_memory():
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, 'r') as f:
            return json.load(f)
    return []

def save_entry(source, prompt, response):
    memory = load_memory()
    memory.append({
        "timestamp": datetime.utcnow().isoformat(),
        "source": source,
        "prompt": prompt,
        "response": response
    })
    with open(MEMORY_FILE, 'w') as f:
        json.dump(memory, f, indent=2)


__author_id__ = "KatchDaVizion_2025_DLC_SIG"

def check_license():
    allowed_user = "David Louis-Charles"
    return allowed_user in __author_id__
