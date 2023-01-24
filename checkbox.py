from tkinter import *

root = Tk()
root.geometry("400x400")
root.title("main")


my_lable = Label(root,text="hello world")
my_lable.pack()

var = IntVar()

check = Checkbutton(root,text="please check this box",variable=var).pack()

def showme():
          myLable = Label(root,text=var.get()).pack()

btn = Button(text='clickme ',command=showme).pack()

root.mainloop()

