from tkinter import *
from PIL import Image,ImageTk

root = Tk()


my_lable = Label(root,text="mark the correct answer")
my_lable.pack()


toppings=[
          ("pepporoni","pepporoni"),
          ("cheese","cheese"),
          ("mushroom","mushroom"),
          ("onion","onion"),
]

pizza = StringVar()
pizza.set("pepporoni")

for key,val in toppings:
          Radiobutton(root,text=key,variable=pizza,value=val).pack(anchor=W)

def clicked(value):
          my_lable = Label(root,text=value)
          my_lable.pack()






my_btns = Button(root,text="click me!",command=lambda:clicked(pizza.get()))
my_btns.pack()
root.mainloop()

