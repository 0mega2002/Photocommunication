from tkinter import messagebox, filedialog
import serial
import base64
import json
import datetime
import os
import logging


def callback(ser, window):
    ser.close()
    window.destroy()


def clicked(txt, ser, parser):
    data = (base64.b64encode(bytes(txt.get(), "utf-8")))
    data2 = str(data)
    data2 = data2.replace("=","")
    checksum = 0
    codeinbin = ""
    sumbin = 0
    for i in data2[2:-1]:
        checksum += ord(i)
        codeinbin += str(bin(ord(i)))[2:]
    for i in codeinbin:
        sumbin += int(i)
    if sumbin % 2 == 0:
        parity = 1
    else:
        parity = 0
    data2 = data2.encode()
    time = datetime.datetime.now().time()
    alljsondata = {"d": str(data2)[2:-1], "c": str(checksum)[-3:], "p": str(parity), "t": str(time)[:-10]}
    with open("data_file.json", "w") as write_file:
        json.dump(alljsondata, write_file)
    with open("data_file.json", "r") as read_file:
        completedata = json.load(read_file)
    text = str(base64.b64encode(str(completedata).encode()))[2:-1].replace("=","")
    text2 = bytes(text,"utf-8")
    
    ser.write(text2)
    print (text2)
    messagebox.showinfo(parser.get("default", "title"), "Text is being sent,\n the checksum is: " + str(checksum)[-3:])
    logging.debug(text)
    logging.info("Text sent")


def clicked3(portsSpinbox, com, parser):
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


def clicked4(ser, parser):
    File = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select file")
    logging.debug(File)
    logging.info("File sent")
    with open(File, "rb") as file:

        data = (base64.b64encode(file.read()))
        data2 = str(data)
        checksum = 0
        codeinbin = ""
        sumbin = 0
        for i in data2[2:-1]:
            checksum += ord(i)
            codeinbin += str(bin(ord(i)))[2:]
        for i in codeinbin:
            sumbin += int(i)
        if sumbin % 2 == 0:
            parity = 1
        else:
            parity = 0
        time = datetime.datetime.now().time()
        alljsondata = {"d": str(data)[2:-1], "c": str(checksum)[-3:], "p": str(parity), "t": str(time)[:-10]}
        with open("data_file.json", "w") as write_file:
            json.dump(alljsondata, write_file)
        with open("data_file.json", "r") as read_file:
            completedata = json.load(read_file)
        ser.write(base64.b64encode(str(completedata).encode()))
        messagebox.showinfo(parser.get("default", "title"),
                            "Text is being sent,\n the checksum is: " + str(checksum)[-3:])
        # print(str(base64.b64encode(str(completedata).encode()))[2:-1])
