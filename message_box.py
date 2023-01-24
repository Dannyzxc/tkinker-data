from tkinter import *
from tkinter import messagebox

root = Tk()

# showinfo, showwarning,showerror,askquestion, askokcancel,askyesno


def popup():
          # messagebox.showinfo("this is my popup","hello world")
          # messagebox.showwarning("this is my popup","hello world")
          # messagebox.showerror("this is my popup","hello world")
          # messagebox.askquestion("this is my popup","hello world")
          # messagebox.askokcancel("this is my popup","hello world")
          res = messagebox.askyesno("this is my popup","hello world")
          Label(root,text=res).pack()


          if res == 1:
                    Label(root,text="proced").pack()

          else:
                    Label(root,text="stop").pack()



Button(root,text="popup",command=popup).pack()

Button(root,text="exit",command=root.quit).pack()


root.mainloop()

