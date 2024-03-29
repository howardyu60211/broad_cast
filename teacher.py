import socket
import threading
import tkinter as tk
from tkinter import (HORIZONTAL, LEFT, NW, Button, Label, PhotoImage, X,
                     messagebox)
from tkinter.ttk import Progressbar


class socket_windows () :

    def __init__(self) :
        self.online_student_name = []
        self.do_lock_windows = False
        self.do_info_windows = False
        self.old_info_label = ""
        self.info_locking = ""
        self.root = tk.Tk()
        self.root.title("< = 廣播系統 = >")
        self.root.geometry('%dx%d+%d+%d' % (500, 500, (self.root.winfo_screenwidth() - 500)/2, (self.root.winfo_screenheight() - 500)/2))
        self.main_tools_label = Label(self.root,relief="raised")
        self.main_lock_pic = PhotoImage(file=r"pic\lock.png")
        self.main_unlock_pic = PhotoImage(file=r"pic\unlock.png")
        self.main_info_pic = PhotoImage(file=r"pic\info.png")
        self.main_socket_pic = PhotoImage(file=r"pic\socket.png")
        self.main_unlock_buttom = Button(self.main_tools_label, image=self.main_unlock_pic, command = self.running).pack(side=LEFT,padx=10)
        self.main_lock_buttom = Button(self.main_tools_label, image=self.main_lock_pic, command = self.cut_running).pack(side=LEFT)
        self.main_info_buttom = Button(self.main_tools_label, image=self.main_info_pic, command = self.info).pack(side=LEFT,padx=10)
        self.main_socket_buttom = Button(self.main_tools_label, image=self.main_socket_pic, command=self.CTS).pack(side=LEFT)
        self.main_tools_label.pack(anchor=NW, fill=X, pady=3)

    def CTS (self) :
        self.connect_to_student = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connect_to_student.bind(('0.0.0.0', 8088))
        print("bind sussesfully ...")
        self.connect_to_student.listen(1)
        print("start connect ...")
        while True :
            conn, addr = self.connect_to_student.accept()
            # 接受數據
            data = conn.recv(1024)
            print("Student in %s has connect..." % (str(addr)))
            self.online_student_name.append(str(addr))

    def running(self) :
        if not(self.do_lock_windows) :
            self.runwindows = tk.Toplevel()
            self.runwindows.title("locking...")
            def close_windows () :
                self.do_lock_windows = False
                self.runwindows.destroy()
            self.runwindows.geometry("240x103+800+100")
            self.runpiclabel = PhotoImage(file=r"pic\Exclamation mark.png")
            self.runwords = Label(self.runwindows, text="running...", image=self.runpiclabel, compound="top", bg="yellow").pack(pady=10)
            self.runshowrunning = Progressbar(self.runwindows,length=59,mode="indeterminate",orient=HORIZONTAL)
            self.runshowrunning.pack()
            self.runshowrunning.start()
            self.do_lock_windows = True
            self.runwindows.protocol("WM_DELETE_WINDOW", close_windows)
            self.runwindows.mainloop()
        else :
            messagebox.showerror("","It's locking now...")
    
    def info (self) :
        if not(self.do_info_windows) :
            self.infowindows = tk.Toplevel()
            self.infowindows.title("info...")
            self.infowindows.geometry("100x100")
            self.do_info_windows = True
            def close_windows () :
                self.do_info_windows = False
                self.infowindows.destroy()
            self.infowindows.protocol("WM_DELETE_WINDOW", close_windows)
            if self.do_lock_windows == True :
                self.info_locking = "locking: True"
            else :
                self.info_locking = "locking: False"
            self.infolabel = Label(self.infowindows,text=self.info_locking,bg="gray", fg="red").pack(fill=X)
            self.old_info_label = self.info_locking
        else :
            messagebox.showerror("", "It's showing ...")
        if self.do_lock_windows == True :
            self.info_locking = "locking: True"
        else :
            self.info_locking = "locking: False"
        if self.old_info_label != self.info_locking :
            self.infolabel = Label(self.infowindows,text=self.info_locking,bg="gray", fg="red").pack(fill=X)
            self.old_info_label = self.info_locking

    def cut_running(self) :
        if self.do_lock_windows == True :
            self.runwindows.destroy()
            self.do_lock_windows = False
        else :
            messagebox.showerror("","no any windows to destroy ...")

a = socket_windows()
