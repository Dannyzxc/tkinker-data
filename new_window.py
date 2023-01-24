from tkinter import *
from PIL import Image ,ImageTk

root = Tk()
root.title("main")



def open():
          # my_imag needs to be global or python will consider it as local for different window
          global my_imag
          top = Toplevel()
          top.title('sub')

          lable_1 = Label(top,text="hello world").pack()
          my_imag = ImageTk.PhotoImage(Image.open("img/img2.png"))
          my_label = Label(top,image=my_imag).pack()
          # btn2 = Button(top,text='close',command=top.quit).pack()
          btn2 = Button(top,text='close',command=top.destroy).pack()




btn= Button(root,text='window',command=open).pack(           )

root.mainloop()

