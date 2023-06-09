from tkinter import *
from tkinter.ttk import*
from tkinter import messagebox
from registerPage_server import LoginPage
from AdminPage_server import AdminPage

import json
import dataSQL
import socket
import threading

FONT_TEXT = ("arial",16,"bold")

# SOCKET..........
SOCKET_SERVER = "127.0.0.1"
SOCKET_PORT = 62402
HEADER = 64
FORMAT = "utf8"
DISCONNECT = "x"
BUFSIZ = 32768

# Option
ADMIN = "an"
PASS = "123"

LOGIN = "Login"
FIND = "Person"
LOGOUT = "Logout"
SHOW = "Info"
DOWLOAD = "dowload"
QUIT = "quit"

# Connect Socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind( (SOCKET_SERVER,SOCKET_PORT) )
s.listen(10)

# global
acc = []

def findPerson(conn_data, conn_socket):
    
    mssv = conn_socket.recv(BUFSIZ).decode(FORMAT)
    print("Mssv", mssv)
    res = dataSQL.findMssvMemver(conn_data, mssv)
    print("data: \n", res)

    if res != []:   
        valid = 1
        name = res[0][0]
        mssv = res[0][1]
        phone = res[0][2]
        email = res[0][3]
        avatar = res[0][4]
    else:
        valid = 0
        name = ""
        mssv = ""
        phone = ""
        email = ""

    people ={
        "Valid": valid, 
        "Name": name, 
        "MSSV": mssv, 
        "Phone": phone, 
        "Gmail": email, 
    }

    print(people)  

    people_data = json.dumps(people) # dong goi du lieu
    people_sz = str(len(people_data)) # cho biet kich thuoc du lieu
    print("data size: ", people_sz)

    conn_socket.sendall(bytes(people_sz, FORMAT)) # gui tin nhan dau tien

    conn_socket.recv(BUFSIZ).decode(FORMAT) # nhan tin nhan rep

    conn_socket.sendall(bytes(people_data, FORMAT)) # gui tin nhan ve data
    
    if valid == 1: # neu co du lieu
        msg = conn_socket.recv(BUFSIZ).decode(FORMAT)
        
        print("Size avatar: ", len(avatar))
        conn_socket.sendall(bytes(str(len(avatar)), FORMAT)) # gui kich thuoc du lieu anh

        msg = conn_socket.recv(BUFSIZ).decode(FORMAT)

        conn_socket.sendall(avatar) # gui du lieu 
    else:
        return

def dowload(conn_data, conn_socket):
    data = dataSQL.getAllMember(conn_data) # lay du lieu

    for row in data:
        person = {"Name": row[0], "Mssv": row[1]}
        print(person)
        person_data = json.dumps(person) # dong goi du lieu
        person_sz = str(len(person_data)) # kich thuoc kieu du lieu
        print("Data size: ", person_sz)

        # bat dau gui dict
        conn_socket.sendall(bytes(person_sz, FORMAT)) # gui kich thuoc du lieu

        conn_socket.recv(BUFSIZ).decode(FORMAT) # nhan tin nhan rep

        conn_socket.sendall(bytes(person_data, FORMAT)) # gui du lieu

        # bat dau gui avatar
        conn_socket.recv(BUFSIZ).decode(FORMAT) # nhan tin nhan rep

        print("Avatar size: ", len(row[4]))

        conn_socket.sendall(bytes(str(len(row[4])), FORMAT)) # gui kich thuoc anh

        conn_socket.recv(BUFSIZ).decode(FORMAT)

        conn_socket.sendall(row[4]) # gui du lieu anh

        conn_socket.recv(BUFSIZ).decode(FORMAT)



    conn_socket.sendall(bytes("STOP", FORMAT)) # gui cho biet ket thu phien giao dich

def show(conn_data, conn_socket):
    data = dataSQL.getAllMember(conn_data)

    for row in data:
        person = {"Name": row[0], "Mssv": row[1], "Phone": row[2], "Email": row[3]}
        print(person)
        person_data = json.dumps(person) # dong goi du lieu
        person_sz = str(len(person_data)) # kich thuoc du lieu
        print("json sz: ", person_sz)
        print(person_data)
        
        conn_socket.sendall(bytes(person_sz, FORMAT)) # gui kich thuoc du lieu

        conn_socket.recv(BUFSIZ).decode(FORMAT)

        conn_socket.sendall(bytes(person_data, FORMAT)) # gui kich thuoc du lieu

    conn_socket.sendall(bytes("STOP", FORMAT)) # gui tin cho biet ket thuc phien gui

def logoutClinet(conn_data, conn_socket):
    conn_socket.sendall(bytes("ok", FORMAT)) 
    user =  conn_socket.recv(BUFSIZ).decode(FORMAT) # nhan ten user tu client
    print("user: ",user)
    i = 0
    for row in acc:
        if row[0] == user:
            acc.pop(i) # tim kiem va xoa tai khoan
            break
        else:
            i += 1
        
    return

def loginClient(conn_data, conn_socket):
    user = conn_socket.recv(BUFSIZ).decode(FORMAT) # nhan ten dang nhap
    print("user: ", user)

    conn_socket.sendall(bytes("--OK--",FORMAT)) 

    pasw = conn_socket.recv(BUFSIZ).decode(FORMAT) # nhan pass
    print("passworld: ", pasw)

    data = dataSQL.isValidUser(conn_data, user) # lay du lieu
    
    for row in data:
        acc.append(row)
        if(pasw == row[1]):
            conn_socket.sendall(bytes("OK",FORMAT)) # so sanh va gui thong bao client biet
            break

# Receive mssage from clinent and do it
def recvFromClient(conn_socket,addr_client):
    while True:
        msg = conn_socket.recv(BUFSIZ).decode(FORMAT) # nhan tin nhan lenh thuc hien tu client
        print("Client talk: ", msg)
        conn_data = dataSQL.conectDatabase()
        if msg == FIND:
            findPerson(conn_data, conn_socket)
        elif msg == LOGIN:
            loginClient(conn_data, conn_socket)
        elif msg == SHOW:
            show(conn_data, conn_socket)
        elif msg == DOWLOAD:
            dowload(conn_data, conn_socket)
        elif msg == LOGOUT:
            logoutClinet(conn_data, conn_socket)
        elif msg == QUIT:
            break
    
    print("end-thread")
    conn_socket.close()
     
# Run SERVER 
def runSever():
    try:
        print("WELLCOM TO GROUP BAD GUY SERVER")
        print(SOCKET_SERVER)
        print("Waiting for client")

        while(True):
            print("Threading......")

            conn_socket, addr_client = s.accept() # chap nhan  ket noi client

            # Threading 
            thread_client = threading.Thread(target=recvFromClient, args=(conn_socket,addr_client))
            thread_client.daemon = True
            thread_client.start()

            print("END CONNECT")
    except KeyboardInterrupt:
        print("ERROR")
        s.close()
    finally:
        s.close()
        print("END PROGRAMING")

def logOut():
    frame_ad.destroy()
    frame_lg = LoginPage(phonebook)
    frame_lg.login_button.configure(command= lambda:logIn(frame_lg)) # chuyen toi ham

def refresh_admin(frame_ad, acc):
    frame_ad.listbox.delete(0, len(acc)) # xoa du lieu o list box
    print(len(acc))
    print(acc)
    for i in range(len(acc)):
        frame_ad.listbox.insert(i, acc[i][0] + "---" + acc[i][1]) # add tai khoan dang ton tai

def connect_admin():

    frame_lg.destroy()
    global frame_ad 
    frame_ad = AdminPage(phonebook)
    frame_ad.bt_logg_out.configure(command= logOut)
    frame_ad.bt_ref.configure(command=lambda: refresh_admin(frame_ad, acc)) # toi ham
    
def logIn(frame):

        user = frame.user_entry.get()
        pswd = frame.pass_entry.get()

        if user == ADMIN and pswd == PASS:
            messagebox.showinfo("Information","Success LogIn")
            # threading runserver
            server_thread = threading.Thread(target=runSever)
            server_thread.daemon = True
            server_thread.start()
            connect_admin()
            
        else:
            messagebox.showerror("Error","Invalid username or password")

def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        phonebook.destroy()


def main():
    global phonebook
    phonebook = Tk()
    phonebook.title("SERVER")
    phonebook.protocol("WM_DELETE_WINDOW",on_closing)
    phonebook.geometry("650x550+350+200")
    phonebook.resizable(False,False)

    global frame_lg

    frame_lg = LoginPage(phonebook)
    frame_lg.login_button.configure(command= lambda:logIn(frame_lg))
    phonebook.mainloop()

    


if __name__ == '__main__':
    main()