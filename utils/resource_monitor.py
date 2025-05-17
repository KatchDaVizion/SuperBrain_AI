# SuperBrain AI Platform
# Created by David Louis-Charles (GitHub: KatchDaVizion)
# © 2025 All Rights Reserved — https://github.com/KatchDaVizion

# utils/resource_monitor.py
import psutil
import time
from utils.logger import log_warning, log_info

def check_disk_space(threshold_percent=90):
    try:
        disk = psutil.disk_usage('/')  # Check root partition, adjust as needed
        if disk.percent > threshold_percent:
            log_warning(f"Disk space nearing critical levels: {disk.percent}% used.", module="resource_monitor")
            return True
        return False
    except Exception as e:
        log_warning(f"Error checking disk space: {e}", module="resource_monitor")
        return False

def check_cpu_usage(threshold_percent=95, duration=1):
    try:
        cpu_percent = psutil.cpu_percent(interval=duration)
        if cpu_percent > threshold_percent:
            log_warning(f"CPU usage high: {cpu_percent}% for {duration} second(s).", module="resource_monitor")
            return True
        return False
    except Exception as e:
        log_warning(f"Error checking CPU usage: {e}", module="resource_monitor")
        return False

def check_memory_usage(threshold_percent=90):
    try:
        memory = psutil.virtual_memory()
        if memory.percent > threshold_percent:
            log_warning(f"Memory usage high: {memory.percent}% used.", module="resource_monitor")
            return True
        return False
    except Exception as e:
        log_warning(f"Error checking memory usage: {e}", module="resource_monitor")
        return False

def monitor_resources(check_interval=60):
    log_info("Resource monitor started.", module="resource_monitor")
    while True:
        check_disk_space()
        check_cpu_usage()
        check_memory_usage()
        time.sleep(check_interval)

if __name__ == "__main__":
    monitor_resources()


__author_id__ = "KatchDaVizion_2025_DLC_SIG"

def check_license():
    allowed_user = "David Louis-Charles"
    return allowed_user in __author_id__
