# SuperBrain AI Platform
# Created by David Louis-Charles (GitHub: KatchDaVizion)
# © 2025 All Rights Reserved — https://github.com/KatchDaVizion

# utils/memory_manager.py
import os
import json
from datetime import datetime
from utils.logger import log_info, log_error

MEMORY_FILE = "../memory/memory_db.json"
os.makedirs(os.path.dirname(MEMORY_FILE), exist_ok=True)

def load_memory():
    try:
        if os.path.exists(MEMORY_FILE):
            with open(MEMORY_FILE, "r") as f:
                return json.load(f)
        else:
            return []
    except json.JSONDecodeError:
        log_error("Error decoding memory file. Starting with empty memory.", module="memory_manager")
        return []
    except Exception as e:
        log_error(f"Error loading memory: {e}", module="memory_manager")
        return []

def save_memory(memory):
    try:
        with open(MEMORY_FILE, "w") as f:
            json.dump(memory, f, indent=2)
        log_info(f"Memory saved to {MEMORY_FILE}", module="memory_manager")
    except Exception as e:
        log_error(f"Error saving memory: {e}", module="memory_manager")

def save_entry(source, prompt, response):
    memory = load_memory()
    memory.append({
        "timestamp": datetime.utcnow().isoformat(),
        "source": source,
        "prompt": prompt,
        "response": response
    })
    save_memory(memory)

def save_local_llm_entry(model_name, content):
    memory = load_memory()
    memory.append({
        "content": content,
        "source": f"local_llm:{model_name}"
    })
    save_memory(memory)


__author_id__ = "KatchDaVizion_2025_DLC_SIG"

def check_license():
    allowed_user = "David Louis-Charles"
    return allowed_user in __author_id__
