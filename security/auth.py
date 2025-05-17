# SuperBrain AI Platform
# Created by David Louis-Charles (GitHub: KatchDaVizion)
# © 2025 All Rights Reserved — https://github.com/KatchDaVizion

def authenticate():
    import getpass
    password = getpass.getpass("Enter assistant password: ")
    if password != "your_secure_password":
        print("❌ Access denied.")
        exit(1)


__author_id__ = "KatchDaVizion_2025_DLC_SIG"

def check_license():
    allowed_user = "David Louis-Charles"
    return allowed_user in __author_id__
