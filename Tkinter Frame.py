from tkinter import *

top =Tk()
top.geometry("600x500")

labelframe1 = LabelFrame(top, text = " Contacts ").pack()

label = Label(top, height = 5, text = " Contacts ", bg = "white", fg = "yellow")
label.place(x = 0, y = 10)
#butt = Button(top, text = "Search").place(x = 1200, y = 10)


#frame = Frame(top, width=1000, height=10, bg="black")
#frame.pack(fill = BOTH, expand = "no", anchor = CENTER)
#labelframe = LabelFrame(frame, text = "Create new contact").pack(fill = BOTH, expand = "yes")

leftframe = Frame(top, width=300, height=200, bg="white").pack(side=LEFT) 

rightframe = Frame(top, width=300, height=200, bg="white").pack(side=RIGHT)


#scrollbar

scrollbar = Scrollbar(top, orient = VERTICAL)
scrollbar.pack(side = RIGHT, fill = Y)

'''
button1 = Button(frame, text="Submit", bg="green", fg="white").pack(side=LEFT)
button2 = Button(frame, text="Remove", bg="brown", fg="white").pack(side=RIGHT)
button3 = Button(frame, text="Add", bg="blue", fg="white").pack(side=LEFT)
button4 = Button(frame, text="Modify", bg="white", fg="black").pack(side=RIGHT)
'''
top.mainloop()
