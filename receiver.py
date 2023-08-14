#!/usr/bin/python3
import subprocess
from sx126x import sx126x
import time
import datetime

# Create sx126x node
node = sx126x(serial_num = "/dev/ttyS0",freq=915,addr=1,power=22,rssi=True,air_speed=2400,relay=False)

try:
    time.sleep(1)
    print("       ┓   ┳┓  ┏┓•  ┏┓┏┓\n\
       ┃ ┏┓┣┫┏┓┃┃┓  ┃ ┏┛\n\
       ┗┛┗┛┛┗┗┻┣┛┗  ┗┛┗━\n\
       -----------------\n\
         Receiver Node\n")

    while True:
        log = open("receiver_node.log", "a")
        clock = datetime.now()

        incoming_data = node.receive()
        if incoming_data:
            command = incoming_data.decode().split(',')
            
            print(f" {clock} Command Received: {command} @ -{node.get_rssi()} dBm")
            log.write(f"{clock} Command Received: {command} @ -{node.get_rssi()} dBm")
            try:
                output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
                print("Command output:\n", output.decode())
                log.write("Command output:\n" + output.decode())
                
            except subprocess.CalledProcessError as e:
                print("Error executing command:", e.output.decode())
                log.write("Error executing command:", e.output.decode())

        time.sleep(1)
        log.close()

except KeyboardInterrupt:
    node.close()
    log.close()
    exit()