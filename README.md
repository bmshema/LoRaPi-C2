# LoRaPi C2
Enables remote command execution on one or more Raspberry Pis over Lora. This is meant for simple command execution such as rebooting a remote node or executing pre-staged scripts for various functions.

## Hardare Requirements:
This was built for the Waveshare SX1262 868M LoRa Hat on Raspberry Pi 4B. The C2 can either be another Raspberry Pi or a laptop with the SX1262 connected to USB.

Connect the SX1262 to the Raspberry Pi according to vendor instructions and set the jumper caps to "B".

## Installation:
##### Linux:
```
$ sudo apt install python3 python3-pip
$ git clone https://github.com/bmshema/pi-C2-over-LoRa.git
$ cd LoRaPi_C2
$ pip install -r requirements.txt
```

