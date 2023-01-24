from tkinter import *


root = Tk()
root.title("tkinker man")
root.iconbitmap('img/icon1.ico')



btn_quit = Button(root,text="exit",command=root.quit)
btn_quit.pack()


root.mainloop()

