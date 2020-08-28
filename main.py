import serial
import keyboard
import platform


if platform.system() == "Darwin":
    LEFT_KEY = 123
    UP_KEY = 126
    RIGHT_KEY = 124
    DOWN_KEY = 125

if platform.system() == "Windows":
    LEFT_KEY = 75
    UP_KEY = 72
    RIGHT_KEY = 72
    DOWN_KEY = 80

ser = serial.Serial('/dev/tty.usbmodemS_N__G16M02291', timeout=1)

while True:
    line = ser.readline()
    if len(line) > 0:
        line_str = line.decode('utf-8')[:-1]  # last char is /n

        keyboard.write(line_str)
        keyboard.send(124)
        keyboard.send(123)
        keyboard.send(123)
        break

ser.close()
