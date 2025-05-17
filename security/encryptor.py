# SuperBrain AI Platform
# Created by David Louis-Charles (GitHub: KatchDaVizion)
# © 2025 All Rights Reserved — https://github.com/KatchDaVizion

from cryptography.fernet import Fernet
import json

KEY_FILE = "security/secret.key"

def generate_key():
    key = Fernet.generate_key()
    with open(KEY_FILE, 'wb') as f:
        f.write(key)

def load_key():
    return open(KEY_FILE, 'rb').read()

def encrypt_file(file_path):
    key = load_key()
    f = Fernet(key)
    with open(file_path, 'rb') as file:
        encrypted = f.encrypt(file.read())
    with open(file_path, 'wb') as file:
        file.write(encrypted)

def decrypt_file(file_path):
    key = load_key()
    f = Fernet(key)
    with open(file_path, 'rb') as file:
        decrypted = f.decrypt(file.read())
    with open(file_path, 'wb') as file:
        file.write(decrypted)


__author_id__ = "KatchDaVizion_2025_DLC_SIG"

def check_license():
    allowed_user = "David Louis-Charles"
    return allowed_user in __author_id__
