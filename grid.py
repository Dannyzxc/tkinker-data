from tkinter import *

root = Tk()

# creating a lable  widget
my_lable1 = Label(root,text="hello world")
my_lable2 = Label(root,text="my name is Dnyaneshwar  ")
my_lable3 = Label(root,text="                                                                            ")
my_lable4 = Label(root,text="this is a computer")

# oops approach
my_lable5 = Label(root,text="thank you").grid(row=1,column=2)
# showing it on the screen
my_lable1.grid(row=0,column=0)
my_lable2.grid(row=1,column=0)
my_lable3.grid(row=0,column=1)
my_lable4.grid(row=1,column=1)

root.mainloop()

