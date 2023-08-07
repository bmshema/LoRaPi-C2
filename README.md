# LoRaPi C2
Enables remote command execution on one or more Raspberry Pis over Lora. This is meant for simple command execution such as rebooting a remote node or executing pre-staged scripts for various functions.

## Hardare Requirements:
This was built for the Waveshare SX1262 868M LoRa Hat on Raspberry Pi 4B. The C2 can either be another Raspberry Pi or a laptop with the SX1262 connected to USB.

Connect the SX1262 to the Raspberry Pi according to vendor instructions and set the jumper caps to "B".

## Installation:
#### Linux C2 / Remote Nodes:
```
$ sudo apt install python3 python3-pip
$ git clone https://github.com/bmshema/pi-C2-over-LoRa.git
$ cd LoRaPi_C2
$ pip install -r requirements.txt
```
#### Windows (If using a Windows machine for C2):
- Install SX1262 drivers per vendor's instructions.
- Connect to SX1262 via USB and set jumper caps to "A", M1, and M0.
- Install Python3
```
$ git clone https://github.com/bmshema/pi-C2-over-LoRa.git
$ cd LoRaPi_C2
$ pip install -r requirements.txt
```
## Usage:
### "Commander Node":
```
sudo python3 commander.py
```
- Press "c" to send a command.
- Commands should be structured as "nodeAdress,frequncy,command"
- Example: 1,915,ls -alh
- Press enter. Press "c" to run another command.

By default, the commander is node address 0 and the receiver is node address 1 at 915MHz. Change the frequency on line 14 to comply with your regional RF regulations.
```python
node = sx126x(serial_num = "/dev/ttyS0",freq=915,addr=0,power=22,rssi=True,air_speed=2400,relay=False)
```
- If running commander.py from a Linux-based laptop change "/dev/ttyS0" to "/dev/ttyUSB0". This could be different depending on your system and what other devices might be connected.
- If running commander.py from windows, change "/dev/ttySO" to the appropriate COM port.

### "Receiver Node":
The receiver node is address 1 by default. For multiple receiver nodes, you may change the node address on line 7 for each additional node.
```python
node = sx126x(serial_num = "/dev/ttyS0",freq=915,addr=0,power=22,rssi=True,air_speed=2400,relay=False)
```
For testing, ssh to your receiver node and run:
```bash
sudo python3 receiver.py
```
Nothing exciting will happen until you send a command from your commander node. Run "ls" or some other simple command to ensure you see the output of that command on your receiver node's terminal.

Since this node is meant to be remote and at a distance away, receiver.py should be run as a service at boot. 

Using systemd as an example, create a file called receiver.service on your remote node at /etc/systemd/system/ with the following contents:
```bash
[Unit]
Description=LoRaPi-C2 Service
After=multi-user.target
Environment=PYTHONUNBUFFERED=1

[Service]
Type=simple
ExecStart=/usr/bin/python3 /home/pi/LoRaPi-C2/receiver.py
Restart=on-failure
RestartSec=5
TimeoutStartSec=infinity

[Install]
WantedBy=multi-user.target

```
Modify the ExecStart field to reflect the path to your python3 executable and the path on your machine to receiver.py

##### Start and Enable the service.
```bash
sudo systemctl start receiver.service
sudo systemctl enable receiver.service
```




## Warning: Always comply with your national radio frequency usage restrictions.

