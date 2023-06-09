from tkinter import *
from PIL import Image, ImageTk

import datetime
import os
import sys

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
        Frame.__init__(self,master)
        # khoi tao
        self.configure(
            bg = "#10c4e8",
            height = 250,
            width = 500,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        master.geometry("500x250")
        self.grid(row=0, column=0, sticky="nsew")

        # tao title cho page
        self.label_title = Label(
                self, 
                text="\nMANAGER CLIENT PHONEBOOK APP\n",
                font="arial 15 bold",
                fg="black",
                bg="#10c4e8"
        )
        self.label_title.place(x=100,y=10)
        # toa hinh anh 
        self.image = ImageTk.PhotoImage(Image.open(path("img.png")))
        self.image_label = Label(self, image=self.image, bg='#10c4e8')
        self.image_label.place(x=10,y=10)

        # tao header date time
        self.data_lbl = Label(
                self, 
                text="Today's "+ date,  
                font='arial 10 bold', 
                bg='#10c4e8',
                fg="black",
                relief='flat'
        )
        self.data_lbl.place(x=360,y=70)
        # tao dong chu USER
        self.user_label = Label(
                self, 
                text="USER",
                font="arial 15",
                fg="#ff0000",
                bg="#10c4e8",
                relief='flat'
        )
        self.user_label.place(x=30,y=120)
        # tao hop de nhap
        self.user_entry = Entry(
                self,
                width= 40,
                bg="#d6d6d6",
                relief="groove"
        )
        self.user_entry.place(x=150,y=120,height=30)

        # tao dong chu PASSWORD
        self.pass_label = Label(
                self, 
                text="PASSWORD",
                font="arial 15",
                fg="#ff0000",
                bg="#10c4e8",
                relief='flat'
        )
        self.pass_label.place(x=30,y=160)
        # tao hop de nhap
        self.pass_entry = Entry(
                self,
                width= 40,
                bg="#d6d6d6",
                relief="groove"
        )
        self.pass_entry.place(x=150,y=160,height=30)

        # tao nut bam de dang nhap
        self.login_button = Button(
                self,
                text="LOG IN",
                bg="#8c8c8c",
                fg='floral white',
                font="arial 10",
                width= 10,
                relief= 'raised'
        )
        self.login_button.place(x=200,y=200)
        # tao cai thong bao khi dang nhap

    

        



        