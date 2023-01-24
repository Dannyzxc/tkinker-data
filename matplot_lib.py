from tkinter import *
import numpy as np
import matplotlib.pyplot as plt

root = Tk()
root.geometry("400x400")
root.title("main")


my_lable = Label(root,text="hello world")
my_lable.pack()

def graph():
          # house_price = np.random.normal(200000,25000,5000)
          # plt.hist(house_price,200)
          # plt.show()

          # house_price = np.random.normal(200000,25000,5000)
          # plt.pie(house_price)
          # plt.show()

          house_price = np.random.normal(200000,25000,5000)
          plt.polar(house_price)
          plt.show()

my_btn = Button(root,text='graph',command=graph)
my_btn.pack()

root.mainloop()

