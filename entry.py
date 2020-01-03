from tkinter import *

root = Tk()

e = Entry(root, width=20, bg="blue", fg="white", borderwidth=5)
e.pack()
e.insert(0, "Enter your Name: ")

def myClick():
	hello = "Hello " + e.get()
	my_label = Label(root, text=hello)
	my_label.pack()

my_button = Button(root, text="Enter your name", command=myClick)
my_button.pack()


root.mainloop()