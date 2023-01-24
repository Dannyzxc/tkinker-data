# incomplete image gallery using tkinter python 


from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("tkinker man")

my_img1 = ImageTk.PhotoImage(Image.open("img/img1.png"))
my_img2 = ImageTk.PhotoImage(Image.open("img/img2.png"))
my_img3 = ImageTk.PhotoImage(Image.open("img/img3.png"))
my_img4 = ImageTk.PhotoImage(Image.open("img/img4.png"))

img_list = [my_img1,my_img2,my_img3,my_img4]


my_lable= Label(image=my_img1)
my_lable.grid(row=0,column=0,columnspan=5)


def forward(data):
          global forward_btn
          global back_btn 
          global my_label 

          my_label.grid_forget()
          btn3 = Button(root,text=">>",padx=30,pady=30,command=lambda: forward(data+1))
          btn1 = Button(root,text="<<",padx=30,pady=30,command=lambda: backword(data - 1))


          my_label = Label(image=img_list[data-1])
          my_label.grid(row=0,column=0,columnspan=5)
          # btn1.grid(row=1,column=0)
          btn3.grid(row=1,column=2)


def backword():
          global forward_btn
          global back_btn 
          global my_label 



btn1 = Button(root,text="<<",padx=30,pady=30,command=lambda: backword)
btn2 = Button(root,text="exit" , command=root.quit,padx=30,pady=30)
btn3 = Button(root,text=">>",padx=30,pady=30,command=lambda: forward(2))

btn1.grid(row=1,column=0)
btn2.grid(row=1,column=1)
btn3.grid(row=1,column=2)


root.mainloop()

