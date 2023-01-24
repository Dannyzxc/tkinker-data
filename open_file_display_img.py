from tkinter import *
from tkinter import filedialog
from PIL import Image,ImageTk

root = Tk()


def open():
          global my_img
          root.filename = filedialog.askopenfilename(initialdir="/tkinker/img",title="select a file ",filetypes=(("png files","*.png"),("all files","*.*")))
          location = root.filename
          my_lable = Label(root,text=location).pack()

          my_img = ImageTk.PhotoImage(Image.open(location))
          my_img_label = Label(image=my_img).pack()


btn = Button(root,text="open file",command=open).pack()
root.mainloop()

