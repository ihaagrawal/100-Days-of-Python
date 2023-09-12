from tkinter import *
windows=Tk()
windows.minsize(width=400,height=400)
windows.title('Miles to Km Convertor')

miles=Label(text="Miles",font=("Comic Sans",16,"bold"))
miles.place(x=300,y=100)

km=Label(text="Km",font=("Comic Sans",16,"bold"))
km.place(x=300,y=150)

user_input=Entry()
user_input.place(x=150,y=100)

com_output=Label(text=0,font=("Arial",16,"normal"))
com_output.place(x=200,y=150)

equal=Label(text="is equal to",font=("Comic Sans",16,"bold"))
equal.place(x=30,y=150)

def on_click():
    mile=int(user_input.get())
    kms=mile*1.6
    com_output.config(text=kms)

calc=Button(text="Calculate",command=on_click)
calc.place(x=180,y=180)


windows.mainloop()