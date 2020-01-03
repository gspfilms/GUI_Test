from tkinter import *

root = Tk()

def myClick():
	my_label = Label(root, text="Look! I clicked a button!")
	my_label.pack()

my_button = Button(root, text="Click Me!", command=myClick, fg="white", bg = "#000000")
my_button.pack()


root.mainloop()