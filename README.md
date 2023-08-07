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
#### "Commander Node":
```
sudo python3 commander.py
```
- Press "c" to send a command.
- Commands should be structured as <node address>,<frequency>,<command>
Example: 1,915,sudo reboot

By default, the commander is node address 0 and the receiver is node address 1 at 915MHz. Change the frequency on line 14 to comply with your regional RF regulations.
```python
node = sx126x(serial_num = "/dev/ttyS0",freq=915,addr=0,power=22,rssi=True,air_speed=2400,relay=False)
```
- If running commander.py from a Linux-based laptop change "/dev/ttyS0" to "/dev/ttyUSB0". This could be different depending on your system and what other devices might be connected.
- If running commander.py from windows, change "/dev/ttySO" to the appropriate COM port.



## Warning: Always comply with your national radio frequency usage restrictions.

