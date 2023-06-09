import socket
from tkinter import*
from tkinter import messagebox
from registerPage_client import LoginPage
from AdminPage_client import AdminPage


HOST = "127.0.0.1"
SERVER_PORT = 62402
FORMAT = "utf8"

FIND = "Person"
LOGIN = "Login"
LOGOUT = "Logout"
QUIT = "quit"
BUFSIZ = 32768

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("CLIENT SLIDE")
client.connect( (HOST, SERVER_PORT) ) 
print("Client address: ", client.getsockname())


def logout():
    client.sendall(bytes(LOGOUT, FORMAT))
    msg = client.recv(1024).decode(FORMAT)
    print(account_user, " removed")
    client.sendall(bytes(account_user, FORMAT))

    frame_hp.destroy()
    frame_lg = LoginPage(phonebook)
    frame_lg.button_login.configure(command=lambda: login(frame_lg))


def home_page():
    frame_lg.destroy()
    global frame_hp
    frame_hp = AdminPage(phonebook, client)
    frame_hp.button_logout.configure(command= logout)

def login(frame):
    try:
        user = frame.user_name_text.get() # lay du lieu
        pasw = frame.pass_name_text.get()
        
        global account_user
        account_user = user 
        if  user =="" or pasw == "":
            messagebox.showerror(message="Fields cannot be empty")
            return

        client.sendall(bytes(LOGIN, FORMAT)) # nhan tin cho server thuc hien login

        # gui user name va passworld cho server de tien hanh kiem tra
        client.sendall(bytes(user, FORMAT))
        print("input: ", user)
        # tuan tu de tranh bi mat du lieu
        client.recv(1024).decode(FORMAT)
        print(" == server is responding ==")
        client.sendall(bytes(pasw, FORMAT))
        print("input: ", pasw)

        msg = client.recv(1024).decode(FORMAT)
        if msg == "OK":
            print(msg)
            messagebox.showinfo("Information","Success LogIn")
            home_page()
        else:
            messagebox.showerror(message="Invalid login, please try again")
            return
    except:
        messagebox.showerror(message="Server is not responding")
        print("Erorr: server is not responding")

def on_closing():

    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        client.sendall(bytes(QUIT, FORMAT)) # ket thuc mot phien giao tiep
        phonebook.destroy()

def main():
    try:
        global phonebook
        phonebook = Tk()
        phonebook.title("Client")
        phonebook.protocol("WM_DELETE_WINDOW",on_closing)
        phonebook.resizable(False, False)
        phonebook.geometry("650x550")

        global frame_lg
        frame_lg = LoginPage(phonebook)
        frame_lg.button_login.configure(command=lambda: login(frame_lg))
        phonebook.mainloop()
    except:
        print("Error: server is not responding")
        client.close()        
    finally:
        client.close()


if __name__ == '__main__':
    main()