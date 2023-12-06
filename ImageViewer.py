from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("ImageViewer")

image1 = ImageTk.PhotoImage(Image.open("Emma/gettyimages-454252008-612x612.jpg"))
image2 = ImageTk.PhotoImage(Image.open("Emma/gettyimages-1834143713-612x612.jpg"))
image3 = ImageTk.PhotoImage(Image.open("Emma/gettyimages-693924612-612x612.jpg"))
image4 = ImageTk.PhotoImage(Image.open("Emma/gettyimages-1433713705-612x612.jpg"))
image5 = ImageTk.PhotoImage(Image.open("Emma/gettyimages-645737234-612x612.jpg"))
image6 = ImageTk.PhotoImage(Image.open("Emma/gettyimages-1717521091-612x612.jpg"))
image7 = ImageTk.PhotoImage(Image.open("Emma/gettyimages-628353178-612x612.jpg"))

image_list = [image1, image2, image3, image4, image5, image6, image7]

my_label = Label(image=image1)
my_label.grid(row=0, column=0, columnspan=3)

def forward(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number - 1])
    button_forward = Button(root, text=">>", command=lambda: forward(image_number + 1))
    button_back = Button(root, text="<<", command=lambda: back(image_number - 1))
    if image_number < len(image_list):
        button_forward["state"] = NORMAL
    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

    status=Label(root,text="Image"+ str(image_number) +"of "+str(len(image_list)),bd=1,relief=SUNKEN, anchor=E)
    status.grid(row=2,column=0,columnspan=3,sticky=W+E)

def back(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number - 1])
    button_forward = Button(root, text=">>", command=lambda: forward(image_number + 1))
    button_back = Button(root, text="<<", command=lambda: back(image_number - 1))
    if image_number > 1:
        button_back["state"] = NORMAL
    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

    status=Label(root,text="Image"+ str(image_number) +"of "+str(len(image_list)),bd=1,relief=SUNKEN, anchor=E)
    status.grid(row=2,column=0,columnspan=3,sticky=W+E)


button_back = Button(root, text="<<", command=lambda: back(0), state=DISABLED)
button_exit = Button(root, text="Exit", command=root.quit)
button_forward = Button(root, text=">>", command=lambda: forward(2))



button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2,pady=10)


root.mainloop()
