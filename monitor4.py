import psutil
import shutil
import time
from datetime import datetime

log_file = open("system_log.txt", "a")

while True:

    current_time = datetime.now()
    print(f"\nTime: {current_time}")
    log_file.write(f"\nTime: {current_time}\n")

    # CPU
    cpu = psutil.cpu_percent(interval=1)
    print(f"CPU Usage: {cpu}%")
    log_file.write(f"CPU Usage: {cpu}%\n")

    if cpu > 80:
        print("WARNING: CPU usage is very high!")

    # RAM
    ram = psutil.virtual_memory()
    print(f"RAM Usage: {ram.percent}%")
    log_file.write(f"RAM Usage: {ram.percent}%\n")

    if ram.percent > 80:
        print("WARNING: RAM usage is very high!")

    # DISK
    disk = shutil.disk_usage("/")
    used_gb = disk.used // (2**30)
    free_gb = disk.free // (2**30)

    print(f"Disk Used: {used_gb} GB")
    print(f"Disk Free: {free_gb} GB")

    log_file.write(f"Disk Used: {used_gb} GB\n")
    log_file.write(f"Disk Free: {free_gb} GB\n")

    print("Next check in 10 seconds...")
    time.sleep(10)