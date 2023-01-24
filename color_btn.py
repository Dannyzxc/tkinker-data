from tkinter import *

root = Tk()

# def my_click():
#           myLable = Label(root,text="hello")
#           myLable.pack()

my_button1 = Button(root,text="click me",padx=10,pady=10,fg="red",bg='aqua')
my_button2 = Button(root,text="click me",state=DISABLED,bg="white")

my_button1.pack()
my_button2.pack()

root.mainloop()

