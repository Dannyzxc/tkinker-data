from tkinter import *

root = Tk()

root.geometry("400x400")
my_lable = Label(root,text="hello world")
my_lable.pack()

vertical = Scale(root,from_=0,to=200)
vertical.pack()

def slider():
          myLabel1 = Label(root,text=horizontal.get()).pack()
          root.geometry(str(horizontal.get()) + "x400")


horizontal = Scale(root,from_=0,to=800,orient=HORIZONTAL)
horizontal.pack()




myBtn =Button(root,text="click me",command=slider).pack()
root.mainloop()

