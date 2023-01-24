from tkinter import *

root = Tk()

# padx - padding to x axis and pady - padding to y axis
my_button1 = Button(root,text="click me",padx=10,pady=10)
my_button2 = Button(root,text="click me",state=DISABLED)

my_button1.pack()
my_button2.pack()

root.mainloop()

