import psutil

def check_cpu_usage():
    cpu_percent = psutil.cpu_percent()
    if cpu_percent > 80:
        print(f'CPU Usage Alert: {cpu_percent}%')
    else:
        print(f'CPU Usage: {cpu_percent}%')

check_cpu_usage()
