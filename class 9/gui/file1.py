#GUI  -> tkinter module

from tkinter import *

root =Tk()
root.title("Simple Calculator")
root.geometry("300x300")

# Label -> to write something
# Entry -> to take the input from the user
# Button

Label(root,text="My First App").grid(column=0,row=0)

e1 = Entry(root)
e1.grid(column=0,row=1)

e2 = Entry(root)
e2.grid(column=1,row=1)

def addNum():
    a = int(e1.get())
    b = int(e2.get())
    result = a+b
    Label(root,text=result).grid(column=1,row=2)

Button(root,text="ADD",command=addNum).grid(column=0,row=2)

def subNum():
    a = int(e1.get())
    b = int(e2.get())
    result = a-b
    Label(root,text=result).grid(column=1,row=3)

Button(root,text="SUB",command=subNum).grid(column=0,row=3)







root.mainloop()
