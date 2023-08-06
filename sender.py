from sx126x import sx126x
import utils
import time
import termios
import tty
import sys
import select

# Termios setup
old_settings = termios.tcgetattr(sys.stdin)
tty.setcbreak(sys.stdin.fileno())

# Create sx126x node
node = sx126x(serial_num = "/dev/ttyS0",freq=868,addr=0,power=22,rssi=True,air_speed=2400,relay=False)

def send_command():
    get_rec = ""
    print("Input command in the following format:\n")
    print("\033[1;32m0,868,shutdown now\033[0m")
    print("This will send the command to a device with address 0, on frequency 868, to shutdown now\n")

    while True:
        rec = sys.stdin.read(1)
        if rec != None:
            if rec == '\x0a':
                break
            get_rec += rec
            sys.stdout.write(rec)
            sys.stdout.flush()
    
    get_t = get_rec.split(',')
    offset_freq = int(get_t[1])-(850 if int(get_t[1])>850 else 410)

    data = bytes([int(get_t[0])>>8]) + bytes([int(get_t[0])&0xff]) + bytes([offset_freq]) + bytes([node.addr>>8]) + bytes([node.addr&0xff]) + bytes([node.offset_freq]) + get_t[2].encode()

    node.send(data)
    print("\n\033[1;32mCommand sent!\033[0m\n")

try:
    time.sleep(1)
    # Initial prompts
    utils.header()
    print("Press \033[1;32mEsc\033[0m to exit || Press \033[1;32ms\033[0m to send a command\n")

    while True:
        if select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], []):
            c = sys.stdin.read(1)

            # Esc Key detection
            if c == '\x1b':
                break
            # s key detection
            if c == '/x73':
                send_command()

            sys.stdout.flush()
        
        node.receive()

except:
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)

termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)