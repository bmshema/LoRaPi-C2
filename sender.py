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
            pass

except:
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)

termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)