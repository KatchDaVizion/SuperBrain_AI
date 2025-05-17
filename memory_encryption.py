# SuperBrain AI Platform
# Created by David Louis-Charles (GitHub: KatchDaVizion)
# © 2025 All Rights Reserved — https://github.com/KatchDaVizion

import os, json, base64
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.fernet import Fernet

CONFIG_FILE = "memory_config.json"
KEY_FILE = "memory.key"
ENC_FILE = "memory_encrypted.json"

def derive_key_from_passphrase(passphrase: str, salt: bytes) -> bytes:
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(), length=32, salt=salt, iterations=100000, backend=default_backend()
    )
    return base64.urlsafe_b64encode(kdf.derive(passphrase.encode()))

def generate_key_with_passphrase(passphrase: str) -> bytes:
    salt = os.urandom(16)
    key = derive_key_from_passphrase(passphrase, salt)
    with open(KEY_FILE, "wb") as f:
        f.write(salt + b"||" + key)
    return key

def load_key_with_passphrase(passphrase: str) -> bytes:
    if not os.path.exists(KEY_FILE):
        raise FileNotFoundError("memory.key not found")
    with open(KEY_FILE, "rb") as f:
        raw = f.read()
        salt, saved_key = raw.split(b"||")
        derived = derive_key_from_passphrase(passphrase, salt)
        if derived != saved_key:
            raise ValueError("Incorrect passphrase")
        return derived

def encrypt_memory(data: list, fernet_key: bytes):
    f = Fernet(fernet_key)
    return f.encrypt(json.dumps(data).encode())

def decrypt_memory(enc_bytes: bytes, fernet_key: bytes):
    f = Fernet(fernet_key)
    return json.loads(f.decrypt(enc_bytes).decode())


__author_id__ = "KatchDaVizion_2025_DLC_SIG"

def check_license():
    allowed_user = "David Louis-Charles"
    return allowed_user in __author_id__
