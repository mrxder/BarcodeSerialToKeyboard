import serial
import keyboard
import platform
import time
import tkinter as tk
from threading import Thread


def test(x):
    while True:
        val = x.get()
        if len(val) > 0:
            print(x.get())
        time.sleep(1)


window = tk.Tk(className="Scanner Control")
window.geometry("500x200")
# window.configure(bg='blue')
greeting = tk.Label(text="Kostenkonto nr", bg="yellow")
entry = tk.Entry()

greeting.pack()
entry.pack()

scannerThread = Thread(target=test, args=(entry,))
scannerThread.start()

window.mainloop()
exit()


deg Scanner(kostenKontoEntry):
    ser = serial.Serial('COM3', timeout=0.1)

    try:
        while True:
            line = ser.readline()
            if len(line) > 0:
                line_str = line.decode('utf-8')  # last char is /n
                print(line_str)

                kostenKonto = kostenKontoEntry.get()

                if len(kostenKonto) > 0:
                    # blub
                else:
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
        exit()

    ser.close()
    print("Closed by end of program")
    exit()
