import sys
from tkinter import Button, Entry, Label, Spinbox, Tk, ttk
import pip
from configparser import ConfigParser
from func import *

pip.__version__ = 1.0
pip.___author__ = "Giulio Tavera and Edoardo Tinaru"

data = ""
datadict = {}


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

    try:

        com = str(parser.get("default", "port"))
        ser = serial.Serial(port=com, baudrate=int(parser.get("default", "baudrate")), timeout=0, writeTimeout=0)
    except (OSError, serial.SerialException):

        messagebox.showinfo(parser.get("default", "title"), "Could not open " + com)

    window.protocol("WM_DELETE_WINDOW", lambda b=window: callback(b))

    tab_control = ttk.Notebook(window)
    tab1 = ttk.Frame(tab_control)
    tab2 = ttk.Frame(tab_control)
    tab3 = ttk.Frame(tab_control)
    tab_control.add(tab1, text="Receive")
    tab_control.add(tab2, text="Ports")
    tab_control.add(tab3, text="Info")

    lbl1 = Label(tab1, text="Still nothing...")
    lbl1.grid(column=0, row=0)

    portsSpinbox = Spinbox(tab2, from_=0, to=256)
    portsSpinbox.grid(column=0, row=0)

    btn2 = Button(tab2, text="Set port", command=lambda a=com, b=portsSpinbox, c=parser: clicked3(a, b, c))
    btn2.grid(column=1, row=0)
    label5 = Label(tab2, text="Port opened:" + com)
    label5.grid(column=0, row=3)

    btn3 = Button(tab2, text="Ports", command=lambda a=serialPorts, b=parser: clicked2(a, b))
    btn3.grid(column=0, row=1)

    # btn1 = Button(tab1, text="Start receiving", command=lambda a=ser: clicked(a))
    # btn1.grid(column=1, row=1)
    lbl3 = Label(tab3, text="Made by")
    lbl3.grid(column=0, row=0)
    lbl4 = Label(tab3, text="Federico Faggian, Giulio Tavera and Edoardo Tinaru")
    lbl4.grid(column=0, row=1)

    tab_control.pack(expand=1, fill='both')
    # window.bind('<Return>', (lambda e, btn1=btn1: btn1.invoke()))
    if ser.isOpen():
        window.after(100, lambda a=ser, b=window, c=lbl1: receive(a, b, c))
    window.mainloop()


if __name__ == "__main__":
    main()
