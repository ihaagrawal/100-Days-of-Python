from tkinter import *

windows=Tk()
windows.title("My first GUI!")
windows.minsize(width=500,height=500)

def on_click():
    entry_text = inputed.get()
    my_label.config(text=entry_text)

def on_second_click():
    my_label.config(text="Now , I am label")

my_label = Label(text="I am a label", font=("Comic Sans",18,"bold"))
my_label.grid(row=0,column=0)

my_button = Button(text="Click Here", command=on_click)
my_button.grid(row=2,column=2)

inputed=Entry()
inputed.grid(row=5,column=5)

new_button=Button(text='I am new button',command=on_second_click)
new_button.grid(row=0,column=3)




windows.mainloop()