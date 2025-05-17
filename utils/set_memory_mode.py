# SuperBrain AI Platform
# Created by David Louis-Charles (GitHub: KatchDaVizion)
# © 2025 All Rights Reserved — https://github.com/KatchDaVizion

import json

CONFIG_FILE = "memory_config.json"

print("[🧠] SuperBrain Memory Security")
print("1. Enable memory encryption")
print("2. Leave memory unencrypted")
print("3. Cancel")

choice = input("Choose memory mode [1-3]: ").strip()

if choice == "1":
    print("[🔐] Encryption will be enabled.")
    config = {"encrypted": True}
elif choice == "2":
    print("[📝] Memory will remain unencrypted.")
    config = {"encrypted": False}
else:
    print("Cancelled.")
    exit()

with open(CONFIG_FILE, "w") as f:
    json.dump(config, f, indent=4)
print("[✅] Memory mode updated.")


__author_id__ = "KatchDaVizion_2025_DLC_SIG"

def check_license():
    allowed_user = "David Louis-Charles"
    return allowed_user in __author_id__
