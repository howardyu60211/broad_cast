from tkinter import *
import tkinter as tk
import socket

class socket_windows () :
    def __init__(self) :
        self.root = tk.Tk()
        toolsframe = Frame(self.root,relief=RIDGE)
        self.piclabel = PhotoImage(file="pic\lock.png")
        lockbuttom = Button(self.root, image=self.piclabel, command = running_cut)
        lockbuttom.pack()
        #self.connect_to_student = socket.socket
        #self.students_ip = self.connect_to_student.getpeername()
    def running_cut (self) :
        self.runwindows = tk.Toplevel()
        self.runwindows.geometry("150x60")
        self.piclabel = PhotoImage(file="pic\Exclamation mark.png")
        self.words = Label(self.runwindows, text="running...", image=self.piclabel, compound="top")
        self.words.pack()
        self.runwindows.mainloop()
    def maintain(self) :
        self.root.mainloop()

a = socket_windows()
a.maintain()


