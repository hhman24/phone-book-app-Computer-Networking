from tkinter import filedialog
import pyodbc

# Dtabase name....
SERVER_NAME_DATA ="LAPTOP-2PGQ75MC\SQLEXPRESS" 
NAME_DATA = "MMT_Lab"
TABLE_ACCOUNT = "ID_DBS"
TABLE_DBS = "STORE_DBS"

# Connect to Database
def conectDatabase():
    server = SERVER_NAME_DATA
    data = NAME_DATA
    user = "badhair"
    passw = "123"

    conn_data = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+data+';UID='+user+';PWD='+ passw) 
    cursor = conn_data.cursor()
    return cursor

def getAllMember(cursor):
    cursor.execute("SELECT * FROM STORE_DBS")
    #data = cursor.fetchall()# luu duoi dang list
    data  = []
    for row in cursor:
        data.append(row)
    return data

def findNameMember(cursor, name):
    cursor.execute("SELECT * FROM STORE_DBS WHERE Name = ?", name)
    
    data  = []
    for row in cursor:
        data.append(row)
    return data

def findPhoneMember(cursor, phone):
    cursor.execute("SELECT * FROM STORE_DBS WHERE Phone = ?", phone)
    
    data  = []
    for row in cursor:
        data.append(row)
    return data

def findGmailMember(cursor, gmail):
    cursor.execute("SELECT * FROM STORE_DBS WHERE Gmail = ?", gmail)
    
    data  = []
    for row in cursor:
        data.append(row)
    return data

def findMssvMemver(cursor, mssv):
    cursor.execute("SELECT * FROM STORE_DBS WHERE MSSV = ?", mssv)
    
    data  = []
    for row in cursor:
        data.append(row)
    return data 

def isValidUser(cursor, user):
    cursor.execute("SELECT * FROM ID_DBS  WHERE username = ?", user)
    data = []
    for row in cursor:
        data.append(row)
    
    return data

def main():
    conn = conectDatabase()

    data = getAllMember(conn)

    file = filedialog.askdirectory()
        
    if file == None or file == '':
        return

    for row in data:
        file_name = file+ r"\\" + row[1].rstrip() + ".png"
        with open(file_name, 'wb+') as input_file:
            input_file.write(row[4])
            input_file.close()
       
      

if __name__ == '__main__':
    main()