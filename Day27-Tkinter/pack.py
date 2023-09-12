from tkinter import *

windows=Tk()
windows.title("My first GUI!")
windows.minsize(width=500,height=500)

def on_click():
    entry_text = inputed.get()
    my_label.config(text=entry_text)

my_label = Label(text="I am a label", font=("Comic Sans",18,"bold"))
my_label.pack()

my_button = Button(text="Click Here", command=on_click)
my_button.pack()

inputed=Entry()
inputed.pack()



windows.mainloop()