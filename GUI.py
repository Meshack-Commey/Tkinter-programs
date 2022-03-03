from tkinter import *

#creating the application main window.
top = Tk()
#Entring the event main loop
"""
redbutton = Button(top, text = "Red", fg = "red")
redbutton.pack(side = LEFT)
greenbutton = Button(top, text ="Green", fg = "green")
greenbutton.pack(side  = RIGHT)
yellowbutton = Button(top, text ="Yellow", fg ="yellow")
yellowbutton.pack(side = TOP)
blackbutton = Button(top, text = "Black", fg ="black")
blackbutton.pack(side = BOTTOM)
"""
"""
name = Label(top, text ="NAME")
name.grid(row = 0, column = 0)
e1 = Entry(top, text ="Name").grid(row = 0, column = 1)
password = Label(top, text ="Password")
password.grid(row = 1, column = 0)
e2 = Entry(top).grid(row = 1, column = 0)
submit = Button(top, text="Submit").grid(row = 4, column = 0)
"""

top.geometry("400x250")
name = Label(top, text ="Name").place(x=30, y=50)
email = Label(top, text ="Email").place(x=30, y=90)
password = Label(top, text ="Password").place(x=30, y=130)
e1 = Entry(top).place(x=85, y=50)
e2 = Entry(top).place(x=85, y=90)
e3 = Entry(top).place(x=85, y=130)

top.mainloop()
