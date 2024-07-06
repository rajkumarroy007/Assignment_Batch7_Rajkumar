import psutil
 
# Calling psutil.cpu_precent() for 4 seconds
print('The CPU usage is: ', psutil.cpu_percent(4))


CPU_THRESHOLD = 85  # in percentage
CPU_High = 90

def check_cpu_usage():
    # Get the current CPU usage percentage
    cpu_usage = psutil.cpu_percent(interval=1)
    # If CPU usage exceeds the threshold, send an alert
    if cpu_usage > CPU_High:
        print('Alert! CPU usage exceeds threshold: 90%', f'CPU usage is at {cpu_usage}%')
    elif cpu_usage > CPU_THRESHOLD:
        print('Alert! CPU usage exceeds threshold: 85%', f'CPU usage is at {cpu_usage}%')
    # Return the current CPU usage

    return cpu_usage
       
from tqdm import tqdm
from time import sleep
with tqdm(total=100, desc='cpu%', position=1) as cpubar:
    while True:
        cpubar.n=psutil.cpu_percent()
        cpubar.refresh()
        sleep(0.5)
