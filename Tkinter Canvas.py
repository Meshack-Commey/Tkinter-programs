from tkinter import *

top = Tk()
top.geometry("500x250")
c = Canvas(top, width=500,
           height=200,
           bg="white",
           cursor="cross",
           ).grid(row=5, column=0)

top.mainloop()
