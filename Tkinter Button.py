
from tkinter import *

cal = Tk()
cal.geometry("600x400")

buttons = Button(cal, text="My Tkinter Button Design", 
                 width = 50,
                 height = 15,
                 activebackground = "green",
                 activeforeground = "white",
                 bg = "grey",
                 fg = "white",
                 bd = "10px",
                 justify = "right"
                 #command = used-to-call-a-function
                 )

buttons.place(x=100, y=130)


cal.mainloop()
