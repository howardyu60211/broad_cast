import socket
import tkinter as tk
from tkinter import (HORIZONTAL, LEFT, NW, Button, Label, PhotoImage, X,
                     messagebox)
from tkinter.ttk import Progressbar


class socket_windows () :
    def __init__(self) :
        self.locking_windows = False
        self.infoing_windows = False
        self.info_locking = ""
        self.root = tk.Tk()
        self.root.title("<= 廣 播 系 統 =>")
        self.root.geometry("500x500+700+200")
        self.main_tools_label = Label(self.root,relief="raised").pack(anchor=NW, fill=X, pady=3)
        self.main_lock_pic = PhotoImage(file=r"pic\lock.png")
        self.main_unlock_pic = PhotoImage(file=r"pic\unlock.png")
        self.main_info_pic = PhotoImage(file=r"pic\info.png")
        self.main_unlock_buttom = Button(self.main_tools_label, image=self.main_unlock_pic, command = self.running).pack(side=LEFT,padx=10)
        self.main_lock_buttom = Button(self.main_tools_label, image=self.main_lock_pic, command = self.cut_running).pack(side=LEFT)
        self.main_info_buttom = Button(self.main_tools_label, image=self.main_info_pic, command = self.info).pack(side=LEFT,padx=10)
        self.root.mainloop()
        #self.connect_to_student = socket.socket
        #self.students_ip = self.connect_to_student.getpeername()
    def running(self) :
        if not(self.lockingwindows) :
            self.runwindows = tk.Toplevel()
            self.runwindows.title("locking...")
            def close_windows () :
                self.lockingwindows = False
                self.runwindows.destroy()
            self.runwindows.geometry("240x103")
            self.runpiclabel = PhotoImage(file=r"pic\Exclamation mark.png")
            self.runwords = Label(self.runwindows, text="running...", image=self.runpiclabel, compound="top", bg="yellow").pack(pady=10)
            self.runshowrunning = Progressbar(self.runwindows,length=200,mode="indeterminate",orient=HORIZONTAL)
            self.runshowrunning.pack()
            self.runshowrunning.start(interval=10)
            self.lockingwindows = True
            self.runwindows.protocol("WM_DELETE_WINDOW", close_windows)
            self.runwindows.mainloop()
        else :
            messagebox.showerror("","It's locking now...")
    def info (self) :
        if not(self.infoing_windows) :
            self.infowindows = tk.Toplevel()
            self.infowindows.title("info...")
            self.infowindows.geometry("100x100")
        else :
            messagebox.showerror("", "It's showing ...")
            if self.lockingwindows == True :
                self.infolocking = "locking: True"
            else :
                self.infolocking = "locking: False"
            self.infolabel = Label(self.infowindows,text=self.infolocking,bg="gray", fg="red").pack(fill=X)
    def cut_running(self) :
        if self.lockingwindows :
            self.runwindows.destroy()
            self.lockingwindows = False
        else :
            messagebox.showerror("","no any windows to destroy ...")

a = socket_windows()
