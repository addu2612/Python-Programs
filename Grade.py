from tkinter import *

root = Tk()
root.geometry("500x500+10+20")

m1 = Label(root, text="Marks 1:")
m1.pack()
m1entry = Entry(root)
m1entry.pack()

m2 = Label(root, text="Marks 2:")
m2.pack()
m2entry = Entry(root)
m2entry.pack()

m3 = Label(root, text="Marks 3:")
m3.pack()
m3entry = Entry(root)
m3entry.pack()

m4 = Label(root, text="Marks 4:")
m4.pack()
m4entry = Entry(root)
m4entry.pack()


def grade():
    marks1 = int(m1entry.get())
    marks2 = int(m2entry.get())
    marks3 = int(m3entry.get())
    marks4 = int(m4entry.get())
    final = (marks1 + marks2 + marks3 + marks4) / 4
    if final > 90:
        result.config(text="A")
    elif final > 80:
        result.config(text="B")
    elif final > 70:
        result.config(text="C")
    else:
        result.config(text="D")        

b1 = Button(root, text="Submit", command=grade)
b1.pack()

result = Label(root, text="")
result.pack()

root.mainloop()
