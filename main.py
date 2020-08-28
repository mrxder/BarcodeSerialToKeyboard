import serial
import keyboard
import platform


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

print(LEFT_KEY)

#ser = serial.Serial('/dev/tty.usbmodemS_N__G16M02291', timeout=1)
ser = serial.Serial('COM3', timeout=1)

try:
    while True:
        line = ser.readline()
        if len(line) > 0:
            line_str = line.decode('utf-8')[:-1]  # last char is /n

            keyboard.write(line_str)
            keyboard.send("left arrow")
            keyboard.send("left arrow")
            keyboard.send("left arrow")
            keyboard.send("left arrow")
            
            break

except:
    ser.close()

ser.close()
