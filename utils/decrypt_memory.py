# SuperBrain AI Platform
# Created by David Louis-Charles (GitHub: KatchDaVizion)
# © 2025 All Rights Reserved — https://github.com/KatchDaVizion

from memory_encryption import load_key_with_passphrase, decrypt_memory, ENC_FILE
import getpass

try:
    passphrase = getpass.getpass("Enter memory passphrase: ")
    key = load_key_with_passphrase(passphrase)
    with open(ENC_FILE, "rb") as f:
        enc_data = f.read()
    memory = decrypt_memory(enc_data, key)
    for entry in memory:
        print(f"- {entry['timestamp']}: {entry['question']} → {entry.get('response') or entry.get('answer')}")
except Exception as e:
    print(f"[!] Error: {e}")


__author_id__ = "KatchDaVizion_2025_DLC_SIG"

def check_license():
    allowed_user = "David Louis-Charles"
    return allowed_user in __author_id__
