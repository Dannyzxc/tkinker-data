from tkinter import *

root = Tk()
root.geometry("400x400")
root.title("main")


my_lable = Label(root,text="hello world")
my_lable.pack()

def showing():

          my_lable = Label(root,text=clicked.get()).pack()

clicked = StringVar()
clicked.set("mon")
drop = OptionMenu(root,clicked,"mon","tue","wed","thus","fri")
drop.pack()

btn =Button(root,text='click',command=showing).pack()


root.mainloop()

