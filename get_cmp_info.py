import socket
import uuid
import platform
from tkinter import *

screen = Tk()
screen.geometry("500x500")
screen.configure(bg='black')



hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
my_system = platform.uname()


my_label = Label(screen, text='Your computer name is: ' + hostname)
my_label.place(x=40, y=40)

my_label2 = Label(screen, text='Your computer ip address is: ' + IPAddr)
my_label2.place(x=40, y=70)

my_label3 = Label(screen, text="System: " + my_system.node)
my_label3.place(x=40, y=100)

my_label4 = Label(screen, text="Release: " + my_system.release)
my_label4.place(x=40, y=130)

my_label5 = Label(screen, text="Version: " + my_system.version)
my_label5.place(x=40, y=160)

my_label6 = Label(screen, text="Machine: " + my_system.machine)
my_label6.place(x=40, y=190)

my_label7 = Label(screen, text="Processor: " + my_system.processor)
my_label7.place(x=40, y=220)






screen.mainloop()