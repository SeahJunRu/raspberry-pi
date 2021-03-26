import os
import time

import psutil


def temperature_of_raspberry_pi():
    cpu_temp = os.popen("vcgencmd measure_temp").readline()
    return cpu_temp.replace("temp=", "")
 
 
def get_gpio(pin=''):
    gpio_status = os.popen("raspi-gpio get {}".format(pin)).readlines()
    status_type = type(gpio_status)
    return gpio_status

    
# Get cpu statistics
cpu = str(psutil.cpu_percent()) + '%'

# Calculate memory information
memory = psutil.virtual_memory()
# Convert Bytes to MB (Bytes -> KB -> MB)
available = round(memory.available/1024.0/1024.0,1)
total = round(memory.total/1024.0/1024.0,1)	
mem_info = str(available) + 'MB free / ' + str(total) + 'MB total ( ' + str(memory.percent) + '% )'
# Calculate disk information
disk = psutil.disk_usage('/')
# Convert Bytes to GB (Bytes -> KB -> MB -> GB)
free = round(disk.free/1024.0/1024.0/1024.0,1)
total = round(disk.total/1024.0/1024.0/1024.0,1)
disk_info = str(free) + 'GB free / ' + str(total) + 'GB total ( ' + str(disk.percent) + '% )'

print("CPU Info–> ", cpu)
print("Memory Info–>", mem_info)
print("Disk Info–>", disk_info)
print("CPU Temp–>", temperature_of_raspberry_pi())
print("GPIO Status:")
for line in get_gpio(""):
    print('\t', line)