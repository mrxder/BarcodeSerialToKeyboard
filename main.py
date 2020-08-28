import serial
import keyboard
import platform
import time


if platform.system() == "Darwin":
    LEFT_KEY = 123
    UP_KEY = 126
    RIGHT_KEY = 124
    DOWN_KEY = 125

if platform.system() == "Windows":
    LEFT_KEY = "left arrow"
    UP_KEY = "up arrow"
    RIGHT_KEY = "right arrow"
    DOWN_KEY = "down arrow"

#ser = serial.Serial('/dev/tty.usbmodemS_N__G16M02291', timeout=1)
ser = serial.Serial('COM3', timeout=0.1)


try:
    while True:
        line = ser.readline()
        if len(line) > 0:
            line_str = line.decode('utf-8')  # last char is /n
            print(line_str)
            keyboard.write(line_str)
            keyboard.send("right arrow")
            keyboard.send("down arrow")
            time.sleep(0.5)
            keyboard.send("left arrow")
            keyboard.send("left arrow")
            keyboard.send("left arrow")
except:

    ser.close()
    print("Closed by Exception")

ser.close()
print("Closed by end of program")
