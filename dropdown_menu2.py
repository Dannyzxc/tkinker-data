# dropdown using list

from tkinter import *

root = Tk()
root.geometry("400x400")
root.title("main")


my_lable = Label(root,text="hello world")
my_lable.pack()

options = ["mon","tue","wed","thus","fri"]

def showing():
          my_lable = Label(root,text=clicked.get()).pack()


clicked = StringVar()
clicked.set(options[0])
drop = OptionMenu(root,clicked,*options)
drop.pack()

btn =Button(root,text='click',command=showing).pack()


root.mainloop()

