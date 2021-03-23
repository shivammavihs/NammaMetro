from tkinter import *
import mysql.connector
import PathFinding

mydb = mysql.connector.connect(host="localhost", user="root", passwd="Shivam@123", auth_plugin='mysql_native_password', database='login')
mycursor = mydb.cursor()

root = Tk()

def signup():
    mycursor.execute(f"select 'Y' from credentials where userid = '{userid}'")
    res = mycursor.fetchall()
    print(len(res))
    if len(res) == 0:
        mycursor.execute(f"INSERT INTO credentials (userid, password) VALUES ('{userid}', '{password}')")
        mydb.commit()
    else:
        print("Userid already exists")

def login():
    userid = useridvalue.get()
    password = passwordalue.get()
    mycursor.execute(f"select password from credentials where userid = '{userid}'")
    userspassword = mycursor.fetchall()
    print(userspassword[0][0], password)
    if userspassword[0][0] == password:
        print('User logged in')

        source = Label(root, text="Source")
        destination = Label(root, text="Destination")

        source.grid(row=3, column=2)
        destination.grid(row=4, column=2)
        global sourcevalue, destvalue
        sourcevalue = StringVar()
        destvalue = StringVar()

        sourceentry = Entry(root, textvariable=sourcevalue)
        destentry = Entry(root, textvariable=destvalue)

        sourceentry.grid(row=3, column=3)
        destentry.grid(row=4, column=3)

        Button(text="Find route and fare", command=findpath).grid(row=8, column=3)
    else:
        print('invalid Userid/Password')

def findpath():
    sourcest = sourcevalue.get()
    destst=destvalue.get()
    print(sourcest,destst)
    fare, shortestpath = PathFinding.metroNamma.findrouteandfare(sourcest, destst)
    print(fare, shortestpath)



root.geometry("500x500")

userid = Label(root, text="User ID")
password = Label(root, text="Password")

userid.grid(row=1, column=2)
password.grid(row=2, column=2)

useridvalue = StringVar()
passwordalue = StringVar()



useridentry = Entry(root, textvariable=useridvalue)
passwordeentry = Entry(root, textvariable=passwordalue)

useridentry.grid(row=1, column=3)
passwordeentry.grid(row=2, column=3)

Button(text="Login", command=login).grid(row=7, column=3)
Button(text="Sign up", command=signup).grid(row=8, column=3)



root.mainloop()