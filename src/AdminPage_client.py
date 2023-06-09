from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Treeview
from PIL import Image, ImageTk
from findPage_client import FindPage
from dowloadPage_client import DowloadPage
from tkinter import filedialog

import datetime
import os
import sys
import json


FORMAT = "utf8"
BUFSIZ = 32768

SHOW = "Info"
DOWLOAD = "dowload"

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

class AdminPage(Frame):
    def __init__(self, master, client):
        Frame.__init__(self, master)
        #khoi tao
        self.configure(
            bg="red",
            height= 600,
            width= 800,
            bd= 0,
            highlightthickness = 0,
            relief="ridge",
        )
        self.client = client
        self.master = master
        self.master.geometry("800x600")
        self.grid(row=0, column=0, sticky="nsew")

        # frame moi
        self.top = Frame(self, height=100, width=800, bg='#10c4e8')
        self.top.pack(fill=X)

        self.bottom = Frame(self, height=500, width=800, bg='#10c4e8')
        self.bottom.pack(fill=X)

        # toa hinh anh 
        self.image = ImageTk.PhotoImage(Image.open(path("bg3.png")))
        self.image_label = Label(self.top, image=self.image, bg= '#10c4e8')
        self.image_label.place(x=100,y=10)

        # tao heading
        self.heading = Label(
                self.top,
                text='My phone book App', 
                font='arial 20 bold', 
                bg='#10c4e8'
        )
        self.heading.place(x=250,y=20)
        
        # tao ngay thang nam
        self.data_lbl = Label(
                self.top, 
                text="Today's "+ date,  
                font='arial 12 bold', 
                bg='#10c4e8'
        )
        self.data_lbl.place(x=600, y=60)

        # tao button
        # button1 - show list member
        self.show_button = Button(
                self.bottom, 
                text="My people",
                fg='#23bfde', 
                bg='white', 
                font='arial 15 bold',
                command= self.show
        )
        self.show_button.place(x=30, y=30, width=150, height= 50)
        
        # button2 - find person
        self.find_button = Button(
                self.bottom, 
                text="Find people", 
                fg='#23bfde',bg='white', 
                font='arial 15 bold',
                command= self.findPage
        )
        self.find_button.place(x=230, y= 30, width=150, height= 50)
        
        # button3 - dowload avatar
        self.button_dowload_avatar = Button(
                self.bottom, 
                text="Dowload Avatar", 
                fg='#23bfde',bg='white', 
                font='arial 15 bold',
                command= self.dowload
        )
        self.button_dowload_avatar.place(x=430, y= 30, width=160, height= 50)

        # button4 - log out
        self.button_logout = Button(
                self.bottom, 
                text="Log Out", 
                fg='#23bfde',bg='white', 
                font='arial 15 bold'
        )
        self.button_logout.place(x=630, y= 30, width=150, height= 50)

        # tao mot frame chua mot tree view
        self.treeview_frame = Frame(self.bottom, height=400,width=800,bg="black")
        self.treeview_frame.place(x=0,y=100)

        self.treeview = Treeview(self.treeview_frame, height=400, selectmode='browse')
        self.treeview.grid(row=0,column=0)

        self.scroll = Scrollbar(self.treeview_frame, orient=VERTICAL)
        self.scroll.grid(row=0,column=1, sticky= N+S)
        self.treeview.config(yscrollcommand= self.scroll.set)
        self.scroll.config(command= self.treeview.yview)
        

        self.treeview['columns'] = ("Name", "MSSV", "Phone", "Email")
        self.treeview.column('#0', width=0)
        self.treeview.column('Name', anchor="center", width=200, minwidth=20, stretch= True)
        self.treeview.column('MSSV', anchor="center", width=190, minwidth=20, stretch= True)
        self.treeview.column('Phone', anchor="center", width=190, minwidth=20, stretch= True)
        self.treeview.column('Email', anchor="center", width=200, minwidth=20, stretch= True)

        self.treeview.heading("#0", text='')
        self.treeview.heading("Name", text="Name")
        self.treeview.heading("MSSV", text="MSSV")
        self.treeview.heading("Phone", text="Phone")
        self.treeview.heading("Email", text="Email")

    def findPage(self):
        find = FindPage(self.client) # bat cua so tim kiem

    def show(self):
        self.client.sendall(bytes(SHOW, FORMAT))

        people = []
        while True: # buoc vao vong lap
            header = self.client.recv(BUFSIZ).decode(FORMAT) # nhan kich thuoc du lieu

            if ("STOP" in header):
                break

            self.client.sendall(bytes("ok", FORMAT))

            data_sz = int(header)
            data = b""
            while len(data) < data_sz: # nhan du lieu
                packet = self.client.recv(BUFSIZ)
                data +=packet

            person = json.loads(data.decode(FORMAT))
            print(person)
            people.append(person)

        print(len(people))
        print(people)

        for i in self.treeview.get_children(): # xoa du lieu cu
            self.treeview.delete(i)
        
        for i in people: # add du lieu vao tree view 
            name = i["Name"]
            mssv = i["Mssv"]
            phone = i["Phone"]
            email = i["Email"]
            self.treeview.insert(
                parent= '',
                index= 'end',
                text= '',
                values=(
                    name.rstrip(), 
                    mssv.rstrip(), 
                    phone.rstrip(), 
                    email.rstrip() 
                )
            )

    def dowload(self):
        # lay du lieu name, mssv - avatar
        file = filedialog.askdirectory()
        
        if file == None or file == '':
            messagebox.showerror(message="No such directory") 
            return

        self.client.sendall(bytes(DOWLOAD, FORMAT)) # gui tin nhan dowload
        
        pic = []
        
        while True:
            tmp = []
            # doc mot dict 
            header = self.client.recv(BUFSIZ).decode(FORMAT)

            if ("STOP" in header):
                break

            self.client.sendall(bytes("ok", FORMAT))

            data_sz = int(header)
            print(data_sz)
            data = b""
            while len(data) < data_sz:
                packet = self.client.recv(BUFSIZ)
                data +=packet

            person = json.loads(data.decode(FORMAT))
            print(person)
            tmp.append(person)

            # bat dau nhan avatar
            self.client.sendall(bytes("avatar", FORMAT))

            sz_avatar = int(self.client.recv(BUFSIZ).decode(FORMAT))
            print("Avatar size: ", sz_avatar)

            self.client.sendall(bytes("continue", FORMAT))

            avatar = b""
            while len(avatar) < sz_avatar:
                packet = self.client.recv(999999)
                avatar += packet
            
            # luu anh
            file_name = file+ r"\\" + person["Mssv"].rstrip() + ".png"
            with open(file_name, 'wb+') as f:
                f.write(avatar)
                f.close()

            self.client.sendall(bytes("continue", FORMAT))
            # dua du lieu can thiet vao list
            tmp.append(avatar)

            pic.append(tmp)

        for i in pic:
            print(i[0])

        dowload = DowloadPage(pic) # goi cua so dowload
   











        

