import sqlite3 as lite
import random
import string
import tkinter as tk
from tkinter import *
from tkinter import Label, font

def connection(db_name):
    try:
        conn = lite.connect(db_name+'.db')
        c= conn.cursor()
        print("connected to database")
    except:
        print("something went wrong")
        exit()
    return c,conn
    



def password_generate(password_length):
    charcs=list(string.ascii_letters+string.digits+"#@$%&*")
    random.shuffle(charcs)
    password_list=[]
    for i in range(password_length):
        password_list.append(random.choice(charcs))
    password="".join(password_list)
    return password


def dataentry(pointer,conn,email,passw,domain):
    pointer.execute("INSERT INTO user_table (email,password,domain_name) VALUES(?,?,?) ",(email,passw,domain))
    conn.commit()


def data_ret(pointer,domain):
    pointer.execute("SELECT * FROM user_table")
    ansr = pointer.fetchall()
    return ansr

def add():
    ptr,conn=connection("password_db")
    passw=password_generate(int(PWL.get()))
    email=EMAIL.get()
    dmn=Domain.get()
    dataentry(ptr,conn,email,passw,dmn)
    ptr.close()
    Email_entry.delete(0,END)
    PWL_entry.delete(0,END)
    Domain_entry.delete(0,END)

def ret():
    ptr,conn=connection("password_db")
    retr=data_ret(ptr,"")
    #text box

    text_box=tk.Text(root,height=9,width=73)
    text_box.place(x=10,y=140)
    text_box.insert(1.0,retr)

    ptr.close()
    



root=tk.Tk()
root.title("Password Generator")
canvas=tk.Canvas(root,width=600,height=300)
canvas.grid(columnspan=3,rowspan=3)
#text
Email_text=tk.Label(text="EMAIL:")
Domain_name=tk.Label(text="Website:")
PWL=tk.Label(text="Password length:")

PWL.place(x=10,y=100)
Email_text.place(x=10,y=20)
Domain_name.place(x=10,y=60)


EMAIL=StringVar()
Domain=StringVar()
PWL=IntVar()
Email_entry=Entry(textvariable=EMAIL)
Domain_entry=Entry(textvariable=Domain)
PWL_entry=Entry(textvariable=PWL)

PWL_entry.place(x=110,y=100,width="200",height="20")
Email_entry.place(x=110,y=20,width="200",height="20")
Domain_entry.place(x=110,y=60,width="200",height="20")


#add button
add_txt=tk.StringVar()
add_btn=tk.Button(root,textvariable=add_txt,font="Raleway",command=lambda:add())
add_txt.set("ADD")
add_btn.place(x=320,y=25,width="100",height="50")




#ret button
ret_txt=tk.StringVar()
ret_btn=tk.Button(root,textvariable=ret_txt,font="Raleway",command=ret)
ret_txt.set("Retrieve")
ret_btn.place(x=440,y=25,width="100",height="50")



root.mainloop()










