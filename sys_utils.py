#Issue : I named file as psutil.py (which conflicts with the actual psutil library)

import psutil
# function
def system_utils():
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent

    info = {
        "cpu" : cpu,
        "memory" : memory,
        "disk" : disk
    }

    print(info)