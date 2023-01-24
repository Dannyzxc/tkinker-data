from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("tkinker man")

my_img1 = ImageTk.PhotoImage(Image.open("img/img1.png"))

my_lable= Label(image=my_img1)
my_lable.grid(row=0,column=0,columnspan=5)





root.mainloop()

