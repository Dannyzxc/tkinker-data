from tkinter import *

root = Tk()
root.geometry("400x400")
root.title("main")


my_lable = Label(root,text="hello world")
my_lable.pack()

var = StringVar()



check = Checkbutton(root,text="please check this box",variable=var,onvalue="on",offvalue="off")

# deselect the checkbox, because the default is checked
check.deselect()
check.pack()


def showme():
          myLable = Label(root,text=var.get()).pack()

btn = Button(text='clickme ',command=showme).pack()

root.mainloop()

