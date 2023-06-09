from tkinter import*
from PIL import Image, ImageTk

import datetime
import os
import sys

FORMAT = "utf8"
BUFSIZ = 1024 * 4

date = datetime.datetime.now().date()
date = str(date)

def path(file_name):
    file_name = 'pic\\' + file_name
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller _MEIPASS tap mot thu muc va luu tru mot duong dan _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".") # tra ve duong dan path name

    return os.path.join(base_path, file_name) # ket hop mot duong dan voi file name

class LoginPage(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        # khoi tao 
        self.configure(
            bg = "#121212",
            height = 250,
            width = 300,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )
        master.geometry("300x250")
        self.grid(row=0, column=0, sticky="nsew")

        self.image_bg = ImageTk.PhotoImage(Image.open(path("bg2.png")))
        self.image_bg_label = Label(self, image=self.image_bg, bg='#121212')
        self.image_bg_label.place(x=10,y=10)

        # label de gi chu login
        self.login_label = Label(
            self,
            text="Login",
            font="Calibri 40 bold",
            bg="#121212",
            fg="#e0e0e0",
            relief="flat"
        )
        self.login_label.place(x= 120,y=30)

        # tao text de nhap id voi password
        self.user_name_text = Entry(
            self,
            font="Helvetica 12",
            bg="#121212",
            fg="#e0e0e0",
            relief="flat",
            highlightthickness=1
        )
        self.user_name_text.insert(0,"username")
        self.user_name_text.place(x=40, y=120, width=200, height=30)

        self.pass_name_text = Entry(
            self,
            font="Helvetica 12",
            bg="#121212",
            fg="#e0e0e0",
            relief="flat",
            highlightthickness=1
        )
        self.pass_name_text.insert(0,"passworld")
        self.pass_name_text.place(x=40, y=160, width=200, height=30)

        # tao nut bam de login
        self.button_login = Button(
            self,
            bg="#10c4e8",
            fg="#e0e0e0",
            activebackground="#10c4e8",
            relief="flat",
            text="Login",
            font="Calibri 15",
            command= lambda: print("button login")
        )
        self.button_login.place(x=110, y=200, width=80, height=30)
    


            





