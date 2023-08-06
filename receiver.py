import subprocess
from sx126x import sx126x
import time
import sys
import select

# Create sx126x node
node = sx126x(serial_num = "/dev/ttyS0",freq=868,addr=0,power=22,rssi=True,air_speed=2400,relay=False)

try:
    time.sleep(1)

    while True:
        incoming_data = node.receive()
        if incoming_data:
            command = incoming_data.decode().split(',')
            print("Command received:", command)
            
            try:
                output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
                print("Command output:", output.decode())
            except subprocess.CalledProcessError as e:
                print("Error executing command:", e.output.decode())

        time.sleep(1)

except KeyboardInterrupt:
    node.close()
    exit()