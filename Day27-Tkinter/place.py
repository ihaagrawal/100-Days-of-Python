from tkinter import *

windows=Tk()
windows.title("My first GUI!")
windows.minsize(width=500,height=500)

def on_click():
    entry_text = inputed.get()
    my_label.config(text=entry_text)

my_label = Label(text="I am a label", font=("Comic Sans",18,"bold"))
my_label.place(x=0,y=0)

my_button = Button(text="Click Here", command=on_click)
my_button.place(x=200,y=200)

inputed=Entry()
inputed.place(x=350,y=400)



windows.mainloop()