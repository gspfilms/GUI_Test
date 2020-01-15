from tkinter import *

#keydown function
def click():
    entered_text=textentry.get()
    #entered_text=raw_entry.lower
    output.delete(0.0, END)
    try:
        definition = my_compdictionary[entered_text]
    except:
        definition = "sorry I haven't programmed that character yet, please try again. *Try all lowercase names"
    output.insert(END, definition)


#Main
window = Tk()
window.title("Rick and Morty Maaaaaaaaan")
window.configure(background="black")

#My photo
photo1 = PhotoImage(file="morty.gif")
Label (window, image=photo1, bg="black") .grid(row=0, column=0, sticky=E)

#create the label
Label (window, text="Type in your favorite character for their catchphrase...", bg="black", fg="white", font="none 12 bold") .grid(row=2, column=0, sticky=W)

#creates text entry box
textentry = Entry(window, width=20, bg="white")
textentry.grid(row=3, column=0, sticky=W)

# add a submit button
Button(window, text="SUBMIT", width=6, command=click) .grid(row=4, column=0, sticky=W)

#create another label
Label (window, text="\nCatchphrase:", bg="black", fg="white", font="none 12 bold") .grid(row=5, column=0, sticky=W)

#create a text box
output = Text(window, width=75, height=6, wrap=WORD, background="white")
output.grid(row=6, column=0, columnspan=2, sticky=W)

#the dictionary
my_compdictionary = {
    'rick': 'Wubbalubbadubdub!!!', 'tiny rick': "Yo, I'm tiny rick!!!", "morty": "aw geez", "mr. meeseeks": "OOOwweEE",
    'jerry': 'I"m lame Jerry', 'bird person': 'I"m bird person', 'mr. poopy butthole': 'I was murdered'
}

Label (window, text="Click to exit:", bg="black", fg="white", font="none 12 bold") .grid(row=7, column=0, sticky=W)

def close_window():
    window.destroy()
    window.exit()

Button(window, text="Exit", width=14, command=close_window) .grid(row=8, column=0, sticky=W)


window.mainloop()