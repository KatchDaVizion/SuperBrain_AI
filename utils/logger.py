# SuperBrain AI Platform
# Created by David Louis-Charles (GitHub: KatchDaVizion)
# © 2025 All Rights Reserved — https://github.com/KatchDaVizion

# utils/logger.py
import logging
import os
from datetime import datetime

LOGS_DIR = "../logs"
os.makedirs(LOGS_DIR, exist_ok=True)
LOG_FILE = os.path.join(LOGS_DIR, f"superbrain_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log")

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(module)s - %(message)s',
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler()  # Also log to console
    ]
)

logger = logging.getLogger(__name__)

def log_info(message, module=__name__):
    logger.info(f"[{module}] {message}")

def log_warning(message, module=__name__):
    logger.warning(f"[{module}] {message}")

def log_error(message, module=__name__):
    logger.error(f"[{module}] {message}")

def log_debug(message, module=__name__):
    logger.debug(f"[{module}] {message}")


__author_id__ = "KatchDaVizion_2025_DLC_SIG"

def check_license():
    allowed_user = "David Louis-Charles"
    return allowed_user in __author_id__
