from tkinter import *
from PIL import Image, ImageTk
from tkinter.filedialog import asksaveasfile
from tkinter import messagebox

import io
import os 
import sys
import json


FIND = "Person"
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

class ResultFrame(Frame):
    def __init__(self, master, parent,  person):
        Frame.__init__(self, master)
        self.configure(            
            bg = "#23bfde",
            height = 600,
            width = 900,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )
        self.person = person
        self.parent = parent

        # label de hien avatar
        self.label_avatar = Label(self)
        self.label_avatar.place(x=50,y=60, width=400, height=300)
        img_PIL = Image.open(io.BytesIO(self.person[1])).resize((400,300), Image.ANTIALIAS)
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
        self.name_text.place(x=550,y=70, width= 300, height= 30)
        self.name_text.insert(END, self.person[0]["Name"])

        self.label_mssv = Label(
            self, text="Mssv",font="Calibri 15 bold",
            bg="#23bfde",fg="#000000",relief="flat" 
        )
        self.label_mssv.place(x=520,y=120)

        self.mssv_text = Text(self, font='Helvetica 12')
        self.mssv_text.place(x=550,y=150, width= 300, height= 30)
        self.mssv_text.insert(END, self.person[0]["MSSV"])

        self.label_phone = Label(
            self, text="Phone Number",font="Calibri 15 bold",
            bg="#23bfde",fg="#000000",relief="flat" 
        )
        self.label_phone.place(x=520,y=200)

        self.phone_text = Text(self, font='Helvetica 12')
        self.phone_text.place(x=550,y=230, width= 300, height= 30)
        self.phone_text.insert(END, self.person[0]["Phone"])

        self.label_email = Label(
            self, text="Email",font="Calibri 15 bold",
            bg="#23bfde",fg="#000000",relief="flat" 
        )
        self.label_email.place(x=520,y=270)

        self.email_text = Text(self, font='Helvetica 12')
        self.email_text.place(x=550,y=300, width= 300, height= 30)
        self.email_text.insert(END, self.person[0]["Gmail"])

        # tao nut de luu anh va nut quay ve cua so tim kiem
        self.save_button = Button(
            self,
            text="Save",
            font='arial 15 bold',
            fg="black",
            bg="#a8a497",
            command= self.save_img
        )

        self.save_button.place(x=180, y= 380, width=160, height= 50)

        self.back_button = Button(
            self,
            text="Back",
            font='arial 15 bold',
            fg="black",
            bg="#a8a497",
            command= self.back
        )

        self.back_button.place(x=380, y= 500, width=160, height= 50)

    def save_img(self):

        types = [('Portable Network Graphics', '*.png'), ('All Files', '*.*')]
        img_file = asksaveasfile(mode='wb', filetypes=types, defaultextension='*.png')
        if img_file == None:
            return
        img_file.write(self.person[1])

    def back(self):
        self.pack_forget()
        self.parent.geometry("550x120+800+200")
        self.master.tkraise()
        

class FindPage(Toplevel):
    def __init__(self, client):
        Toplevel.__init__(self)

        self.geometry("550x120+800+200")
        self.title("Find Person")
        self.resizable(False,False)
        self.client = client

       
        # frames 
        self.frames = Frame(self, height=550, bg='#23bfde')
        self.frames.pack(fill=X)

        # tao button
        self.find_button_image = ImageTk.PhotoImage(Image.open(path("bg5.png")))
        self.find_button = Button(
            self.frames,
            image=self.find_button_image,
            bg="#23bfde",
            borderwidth=0,
            highlightthickness=1,
            command= self.findPerson,
            relief="flat"
        )
        self.find_button.place(x=430,y= 20)

        self.mssv_entry = Entry(
            self.frames,
            font='Helvetica 15',
            relief="flat",
            bg="#828282",
            fg="#fcfcfc",
            highlightthickness=1
        )
        self.mssv_entry.insert(0,"@Enter MSSV")
        self.mssv_entry.place(x=30, y=40, width=350, height=30)
 
    def findPerson(self):
        people = []
        # gui tin nhan di de tim
        self.client.sendall(bytes(FIND, FORMAT))
        # lay du lieu mssv va gui di
        mssv = self.mssv_entry.get()
        self.client.sendall(bytes(mssv, FORMAT))
        print("Mssv: ", mssv)
        # nhan du lieu ve kich thuoc goi tin
        header = self.client.recv(BUFSIZ).decode(FORMAT)
        data_sz = int(header)

        self.client.sendall(bytes("data", FORMAT))

        data = b""
        print(data_sz)
        while len(data) < data_sz:
            p = self.client.recv(BUFSIZ)
            data += p

        person = json.loads(data.decode(FORMAT))

        if person["Valid"] == 1:
            people.append(person)
            print(people)

            # # nhan du lieu hinh anh avatar
            self.client.sendall(bytes("continue", FORMAT))
            # print("msg")

            sz= int(self.client.recv(100).decode(FORMAT))
            print("Avatar size: ", sz)

            self.client.sendall(bytes("continue", FORMAT))

            avatar = b""
            while len(avatar) < sz:
                packet = self.client.recv(999999)
                avatar += packet

            people.append(avatar)
            print(people)

            result = ResultFrame(self.frames, self, people)
            self.geometry("900x600")
            result.pack(fill=X)
            result.tkraise()
        else:
            messagebox.showerror(message="does not exist")
            return




