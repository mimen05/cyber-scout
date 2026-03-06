import os
import subprocess

def scout():
    print("-" * 30)
    print("CYBER-SCOUT STATUS: ACTIVE")
    print("-" * 30)

    try:
        subprocess.check_output(["ping", "-c", "1", "8.8.8.8"], timeout=2)
        print("Network Status: ONLINE")
    except:
        print("Network Status: OFFLINE")

    downloads = os.path.expanduser("~/Downloads")
    scripts = [f for f in os.listdir(downloads) if f.endswith('.sh')]

    if scripts:
        print(f"Security Status: Found {len(scripts)} script(s) in Downloads!")
    else:
        print("Security Status: No suspicious scripts found.")

    print("-" * 30)

scout()
