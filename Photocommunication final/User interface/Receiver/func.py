#import all the used modules
import base64
from tkinter import messagebox
import serial
import logging
from __init__ import data, datadict


#check all the available com
def clicked2(serialPorts, parser):
    x = "Ports: "
    for i in serialPorts:
        x += str(i)
    messagebox.showinfo(parser.get("default", "title"), x)

#write all the data received from the serial port
def receive(ser, window, lbl1):
    global data, datadict
    while True:
        c = ser.read().decode("ascii") 
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
                datadict["d"] = base64.b64decode(datadict["d"])  
                logging.debug(str(datadict))
                lbl1.delete("1.0","end")
                temp = str(datadict)
                print(temp)
                lbl1.insert("insert",temp)
                logging.info("Package decoded")
                data = ""
            except:
                logging.debug(str(data))
                logging.error("Package syntax error")
            break
        else:
            data += c
    window.after(10, lambda a=ser, b=window, c=lbl1: receive(a, b, c))  
