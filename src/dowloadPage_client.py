from tkinter import *
from PIL import Image, ImageTk


import io
import os 
import sys


FORMAT = "utf8"
BUFSIZ = 32768

def path(file_name):
    file_name = 'pic\\' + file_name
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller _MEIPASS tap mot thu muc va luu tru mot duong dan _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".") # tra ve duong dan path name

    return os.path.join(base_path, file_name) # ket hop mot duong dan voi file name

class DowloadPage(Toplevel):
    def __init__(self, people):
        Toplevel.__init__(self)
        
        self.geometry("800x600")
        self.title("client")
        self.resizable(False,False)
        self.people = people
        
        self.cnt = 0
        # frames 
        self.frames = Frame(self, height=600, bg='#23bfde')
        self.frames.pack(fill=X)

        # label de hien avatar
        self.label_avatar = Label(self)
        self.label_avatar.place(x=50,y=60, width=400, height=300)
        img_PIL = Image.open(io.BytesIO(self.people[0][1])).resize((400,300), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img_PIL)
        self.label_avatar.configure(image=img)
        self.label_avatar.image = img

        # tao hop text de hien thi cac thong tin
        self.label_name = Label(
            self, text="Name",font="Calibri 15 bold",
            bg="#23bfde",fg="#000000",relief="flat" 
        )
        self.label_name.place(x=520,y=40)

        self.name_text = Text(self, font='Helvetica 12')
        self.name_text.place(x=550,y=70, width= 200, height= 30)
        self.name_text.insert(END, self.people[0][0]["Name"].rstrip())

        self.label_mssv = Label(
            self, text="Mssv",font="Calibri 15 bold",
            bg="#23bfde",fg="#000000",relief="flat" 
        )
        self.label_mssv.place(x=520,y=120)

        self.mssv_text = Text(self, font='Helvetica 12')
        self.mssv_text.place(x=550,y=150, width= 200, height= 30)
        self.mssv_text.insert(END, self.people[0][0]["Mssv"].rstrip())

        # tao button 
        self.prev_button = Button(
            self,
            text="Previous",
            font='arial 15 bold',
            fg="black",
            bg="#a8a497",
            command=self.prev
        )

        self.prev_button.place(x=80, y= 500, width=160, height= 50)

        self.Next_button = Button(
            self,
            text="Next",
            font='arial 15 bold',
            fg="black",
            bg="#a8a497",
            command=self.next
        )

        self.Next_button.place(x=600, y= 500, width=160, height= 50)

    def prev(self):

        self.cnt -= 1
        if self.cnt > len(self.people):
            self.cnt += 1
            return


        img_PIL = Image.open(io.BytesIO(self.people[self.cnt][1])).resize((400,300), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img_PIL)
        self.label_avatar.configure(image=img)
        self.label_avatar.image = img
        

        self.name_text.delete(1.0, END)
        self.name_text.insert(END, self.people[self.cnt][0]["Name"].rstrip())
        self.mssv_text.delete(1.0, END)
        self.mssv_text.insert(END, self.people[self.cnt][0]["Mssv"].rstrip())


        
    def next(self):

        self.cnt += 1

        if self.cnt > len(self.people):
            self.cnt -= 1
            return

        img_PIL = Image.open(io.BytesIO(self.people[self.cnt][1])).resize((400,300), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img_PIL)
        self.label_avatar.configure(image=img)
        self.label_avatar.image = img

        self.name_text.delete(1.0, END)
        self.name_text.insert(END, self.people[self.cnt][0]["Name"].rstrip())
        self.mssv_text.delete(1.0, END)
        self.mssv_text.insert(END, self.people[self.cnt][0]["Mssv"].rstrip())

