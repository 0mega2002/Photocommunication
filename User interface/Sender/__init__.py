from func import *
from tkinter import ttk, Button, Tk, Entry, Spinbox, Label
import sys
import pip
from configparser import ConfigParser
import logging

pip.__version__ = 1.0
pip.___author__ = "Giulio Tavera and Edoardo Tinaru"


def main():
    parser = ConfigParser()
    parser.read("default.ini")
    logging.basicConfig(filename='history.log', filemode='w', format='%(asctime)s:%(name)s - %(levelname)s - %('
                                                                     'message)s')
    if parser.get("default", "debug") == '1':
        logging.getLogger().setLevel(logging.DEBUG)
    if parser.get("default", "debug") == '0':
        logging.getLogger().setLevel(logging.INFO)
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    serialPorts = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            serialPorts.append(port)
        except (OSError, serial.SerialException):
            pass

    window = Tk()
    window.title(parser.get("default", "title"))
    window.geometry("300x150")

##    if len(serialPorts) >= 1:
##        try:
##
##            com = str(serialPorts[0])
##            ser = serial.Serial(port=com, baudrate=int(parser.get("default", "baudrate")))
##        except (OSError, serial.SerialException):
##            messagebox.showinfo(parser.get("default", "title"), "Could not open " + com)


    try:

        com = str(parser.get("default", "port"))
        ser = serial.Serial(port=com, baudrate=int(parser.get("default", "baudrate")),write_timeout=0)
    except (OSError, serial.SerialException):

        messagebox.showinfo(parser.get("default", "title"), "Could not open " + com)
        
    tab_control = ttk.Notebook(window)
    tab1 = ttk.Frame(tab_control)
    tab2 = ttk.Frame(tab_control)
    tab3 = ttk.Frame(tab_control)
    tab_control.add(tab1, text="Send")
    tab_control.add(tab2, text="Ports")
    tab_control.add(tab3, text="Info")

    lbl = Label(tab1, text="Please insert in the following label")
    lbl2 = Label(tab1, text="the text you would like to send.")
    lbl.grid(column=2, row=0)
    lbl2.grid(column=2, row=1)

    txt = Entry(tab1, width=20)
    txt.grid(column=2, row=2)
    txt.focus()

    btn1 = Button(tab1, text="Send", command=lambda a=txt, b=ser, c=parser: clicked(a, b, c))
    btn1.grid(column=2, row=3)

    Button(tab1, text="Choose file", command=lambda a=ser, c=parser: clicked4(a, c)).grid(column=3, row=3)

    portsSpinbox = Spinbox(tab2, from_=0, to=256)
    portsSpinbox.grid(column=0, row=0)

    btn2 = Button(tab2, text="Set port", command=lambda a=portsSpinbox, b=com, c=parser: clicked3(a, b, c))
    btn2.grid(column=1, row=0)
    label5 = Label(tab2, text="Port opened:" + com)
    label5.grid(column=0, row=3)

    btn3 = Button(tab2, text="Ports", command=lambda a=serialPorts, c=parser: clicked2(a, c))
    btn3.grid(column=0, row=1)

    lbl3 = Label(tab3, text="Made by")
    lbl3.grid(column=0, row=0)
    lbl4 = Label(tab3, text="Federico Faggian, Giulio Tavera and Edoardo Tinaru")
    lbl4.grid(column=0, row=1)

    tab_control.pack(expand=1, fill='both')
    window.protocol("WM_DELETE_WINDOW", lambda a=ser, b=window: callback(a, b))
    window.bind('<Return>', (lambda e, btn1=btn1: btn1.invoke()))
    window.mainloop()


if __name__ == "__main__":
    main()
