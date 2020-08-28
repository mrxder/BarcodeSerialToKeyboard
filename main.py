import serial
import keyboard

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
