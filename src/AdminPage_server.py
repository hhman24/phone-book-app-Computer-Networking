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

class AdminPage(Frame):
    def __init__(self, master):
        Frame.__init__(self,master)
        #khoi tao
        self.configure(
            bg="red",
            height= 400,
            width= 470,
            bd= 0,
            highlightthickness = 0,
            relief="ridge",
        )

        master.geometry("470x400")
        self.grid(row=0, column=0, sticky="nsew")

        # frame moi
        self.top = Frame(self, height=100, width=470, bg='white')
        self.top.pack(fill=X)

        self.bottom = Frame(self, height=400, width=470, bg='#10c4e8')
        self.bottom.pack(fill=X)
        
        # tao title cho page
        self.label_title = Label(
                self.top, 
                text="\nMANAGER CLIENT PHONEBOOK APP\n",
                font="arial 15 bold",
                fg="black",
                bg="white"
        )
        self.label_title.place(x=100,y=10)
        # toa hinh anh 
        self.image = ImageTk.PhotoImage(Image.open(path("img.png")))
        self.image_label = Label(self.top, image=self.image, bg= 'white')
        self.image_label.place(x=10,y=10)


        # tao list box chua thong tin
        self.frame_listbox = Frame(self.bottom, height=200, width=300, bg="black")
        self.frame_listbox.place(x=50,y=10)
        self.listbox = Listbox(
            self.frame_listbox,
            height=9,
            width=32,
            bg='floral white',
            # activestyle = 'dotbox', 
            font = "Helvetica",
            fg="black",
        )  
        self.listbox.grid(row=0, column=0)
        # tao thanh cuon
        self.scroll = Scrollbar(self.frame_listbox, orient=VERTICAL)
        self.scroll.grid(row=0,column=1, sticky= N+S)
        self.listbox.config(yscrollcommand=self.scroll.set)
        self.scroll.config(command=self.listbox.yview)# de xem
        
        self.listbox.insert(0, "Nothing here")

       

        # #button
        self.bt_ref = Button(
            self.bottom, text="REFRESH", 
            width=12, font='Sans 12 bold',command=lambda: print("Re"))
            
        self.bt_ref.place(x=50,y=250)

        self.bt_logg_out= Button(self.bottom, text="LOG OUT", width=12, font='Sans 12 bold')
        self.bt_logg_out.place(x=300,y=250)




        


    

        



        