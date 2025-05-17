# SuperBrain AI Platform
# Created by David Louis-Charles (GitHub: KatchDaVizion)
# © 2025 All Rights Reserved — https://github.com/KatchDaVizion

import os
import json

MEMORY_FILE = "memory_db.json"

def merge_memory(base_file, merge_file):
    if not os.path.exists(base_file) or not os.path.exists(merge_file):
        print("[!] One or both files are missing.")
        return

    with open(base_file, "r") as f:
        base_data = json.load(f)
    with open(merge_file, "r") as f:
        merge_data = json.load(f)

    combined = {json.dumps(entry): entry for entry in base_data + merge_data}
    final_data = list(combined.values())

    with open(base_file, "w") as f:
        json.dump(final_data, f, indent=2)
    print(f"🔁 Synced memory. {len(final_data)} total entries.")

if __name__ == "__main__":
    print("🔗 Memory Sync Tool")
    base = input("Path to local memory file: ").strip()
    ext = input("Path to external memory file to merge: ").strip()
    merge_memory(base, ext)


__author_id__ = "KatchDaVizion_2025_DLC_SIG"

def check_license():
    allowed_user = "David Louis-Charles"
    return allowed_user in __author_id__
