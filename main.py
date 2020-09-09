import serial
import keyboard
import platform
import time
import tkinter as tk
from threading import Thread


def Scanner(kostenKontoEntry, run):


    ser = serial.Serial('COM3', timeout=0.1)

    multi = 1.0

    try:
        while run[0]:
            line = ser.readline()
            if len(line) > 0:
                line_str = line.decode('utf-8')  # last char is /n
                print(line_str)

                kostenKonto = kostenKontoEntry.get()

                keyboard.write(line_str)
                time.sleep(0.2 * multi)
                
                for i in range(8):
                    keyboard.send("tab")
                    time.sleep(0.05 * multi)
                
                if len(kostenKonto) > 0:
                    keyboard.write(kostenKonto)
                    keyboard.send("enter")
                    time.sleep(0.2 * multi)

                keyboard.send("down arrow")
                time.sleep(0.05 * multi)

                numOfBackTab = 10
                if len(kostenKonto) > 0:
                    numOfBackTab = 11

                for i in range(numOfBackTab):
                    keyboard.send("shift + tab")
                    time.sleep(0.05 * multi)

    except:

        ser.close()
        print("Closed by Exception")
        exit()

    ser.close()
    print("Closed by end of program")
    exit()


window = tk.Tk(className="Scanner Control")
window.geometry("500x200")
# window.configure(bg='blue')
greeting = tk.Label(text="Kostenkonto nr", bg="yellow")
entry = tk.Entry()

greeting.pack()
entry.pack()

run = [True]
scannerThread = Thread(target=Scanner, args=(entry, run,))
scannerThread.start()

window.mainloop()
run[0] = False
