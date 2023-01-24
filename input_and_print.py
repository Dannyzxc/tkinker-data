from tkinter import *

root = Tk()

enter_data = Entry(root,width=50)
enter_data.pack()

# placeholder for input
enter_data.insert(0,"enter your name")

def my_click():
          data = "my name is " + enter_data.get()
          myLable1 = Label(root,text="hello " + enter_data.get())
          myLable1.pack()
          myLable2 = Label(root,text=data)
          myLable2.pack()


my_button1 = Button(root,text="click me",command=my_click,padx=10,pady=10,fg="red",bg='aqua')

my_button1.pack()


root.mainloop()

