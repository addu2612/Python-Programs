import mysql.connector
from tkinter import *

myconn=mysql.connector.connect(host='localhost',user='root',password="12345")

c=myconn.cursor()

c.execute("Create DATABASE FORM")
c.execute("USE FORM")
c.execute("create table response(name varchar(20),email varchar(30),phone int)")

root=Tk()
root.title("MySQL >YourSQL")
root.geometry("300x300")

def submit():
    name=name_textbox.get()
    email=email_textbox.get()
    phone=phone_textbox.get()
    result=f"{name}\n{email}\n{phone}"
    result_label.config(text=result)
    insertq="Insert into response values(%s,%s,%s)"
    val=(name,email,phone)
    c.execute(insertq,val)
    print("Done")


name_label=Label(root,text="Enter Name:")
name_label.pack()
name_textbox=Entry(root)
name_textbox.pack()

email_label=Label(root,text="Enter Email:")
email_label.pack()
email_textbox=Entry(root)
email_textbox.pack()

phone_label=Label(root,text="Enter Phone:")
phone_label.pack()
phone_textbox=Entry(root)
phone_textbox.pack()

b1=Button(root,text="Submit",command=submit)
b1.pack()

root.mainloop()

c.execute("select * from response")
res=c.fetchall()
for row in res:
    print(row)

