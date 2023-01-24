from tkinter import *
from PIL import Image,ImageTk

root = Tk()


my_lable = Label(root,text="mark the correct answer")
my_lable.pack()

r = IntVar()
r.set(2)





def clicked(value):
          my_lable = Label(root,text=value)
          my_lable.pack()

Radiobutton(root,text="option 1",variable =r,value=1,command=lambda:clicked(r.get()) ).pack()
Radiobutton(root,text="option 2",variable =r,value=2,command=lambda:clicked(r.get()) ).pack()
Radiobutton(root,text="option 3",variable =r,value=3,command=lambda:clicked(r.get()) ).pack()
Radiobutton(root,text="option 4",variable =r,value=4,command=lambda:clicked(r.get()) ).pack()




my_btns = Button(root,text="click me!",command=lambda:clicked(r.get()))
my_btns.pack()
root.mainloop()

