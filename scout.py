import os
import subprocess
import shutil

def check_disk():
    total, used, free = shutil.disk_usage("/")
    total_gb = total // (2**30)
    used_gb = used // (2**30)
    free_gb = free // (2**30)

    percent_used = (used / total) * 100
    return f"{used_gb}GB / {total_gb}GB ({percent_used:.1f}% used)" 

def scout():
    print("-" * 30)
    print("CYBER-SCOUT STATUS: ACTIVE")
    print("-" * 30)

    try:
        subprocess.check_output(["ping", "-c", "1", "8.8.8.8"], timeout=2, stderr=subprocess.DEVNULL)
        print("Network Status: ONLINE")
    except:
        print("Network Status: OFFLINE")

    downloads = os.path.expanduser("~/Downloads")
    scripts = [f for f in os.listdir(downloads) if f.endswith('.sh')]

    if scripts:
        print(f"Security Status: Found {len(scripts)} script(s) in Downloads!")
    else:
        print("Security Status: No suspicious scripts found.")

    print(f"Disk Health:   {check_disk()}")

    print("-" * 30)

scout()
