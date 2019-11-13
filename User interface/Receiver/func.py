import base64
from tkinter import messagebox
import serial
import logging
from __init__ import data, datadict


def callback(window):
    # if ser is None:
    window.destroy()
    # else:
    #   ser.close()
    #  window.destroy()


def clicked(ser):
    #    try:
    #        packeddata = eval(base64.b64decode(txt.get().encode()).decode())
    #        logging.debug(str(packeddata))
    #        logging.info("Package decoded")
    #    except:
    #        logging.debug(str(txt))
    #        logging.error("Package syntax error")
    print("")


def clicked3(com, portsSpinbox, parser):
    commanual = "COM" + str(portsSpinbox.get())

    if commanual == com:
        messagebox.showinfo(parser.get("default", "title"), "Port already opened")
    else:
        try:
            # ser = serial.Serial(port = commanual, baudrate=9600)
            messagebox.showinfo(parser.get("default", "title"), "Port " + commanual + " opened")
            # label5 = Label(tab2, text = "Port opened is " + commanual )
        except (OSError, serial.SerialException):
            messagebox.showinfo(parser.get("default", "title"), "Could not open " + commanual)


def clicked2(serialPorts, parser):
    x = "Ports: "
    for i in serialPorts:
        x += str(i)
    messagebox.showinfo(parser.get("default", "title"), x)


def receive(ser, window, lbl1):
    global data, datadict
    while True:
        c = ser.read().decode("ascii")  # attempt to read a character from Serial

        # was anything read?
        if len(c) == 0:
            break
        if c == " ":
            break
        if c == "\n":
            try:
                data.replace(" ", "").replace("\n", "")
                print(type(data))
                print(len(data))
                print("ricevuto " + data)

                while (len(data)-2) % 4 != 0:
                    data.replace(" ", "").replace("\n", "")
                    data += "="
                print("ricevuto con = " + data)

                datadict = eval(base64.b64decode(data.encode()))

                datadict["d"] = datadict["d"][2:-1]
                while len(datadict["d"]) % 4 != 0:
                    datadict["d"] += "="
                datadict["d"] = base64.b64decode(datadict["d"])  # .encode()).decode(
                logging.debug(str(datadict))
                lbl1.config(text=str(datadict))
                logging.info("Package decoded")
                data = ""
            except:
                logging.debug(str(data))
                logging.error("Package syntax error")
            break
        else:
            # print(c,end="")
            data += c
    window.after(10, lambda a=ser, b=window, c=lbl1: receive(a, b, c))  # check serial again soon
