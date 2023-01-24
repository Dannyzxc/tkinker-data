from tkinter import *

root = Tk()
root.title('making frames')

# my_lable = Label(root,text="hello world")

# my_lable.pack()

# padx and pady acts like padding 
frame = LabelFrame(root,text="this is my frame",padx=35,pady=35)

# but in here padx and pady acts like margin
frame.pack(padx=100,pady=100)

btn1 = Button(frame,text="don't click here")
btn1.pack()


root.mainloop()

