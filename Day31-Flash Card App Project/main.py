from tkinter import *
import pandas as pd
import random 
BACKGROUND_COLOR = "#B1DDC6"
CANVAS_BACKGROUND = "#94ADD7"
CANVAS_HIGHLIGHT = "#0D1282"
time_limit=5

#--------------------------- DATA ---------------------------

df=pd.read_csv(".\\french_words.csv")


def choice():
    choice.ind=random.randint(0,102)

def known_words():
    
    my_dict=df.to_dict()
    french_list=my_dict['French'][choice.ind]
    english_list=my_dict['English'][choice.ind]
    
    del my_dict['French'][choice.ind]
    del my_dict['English'][choice.ind]

    known_word_list=pd.DataFrame(my_dict)
    known_word_list.to_csv(".\\known_words.csv")

    run_program()
#--------------------------- UI Setup ---------------------------

windows=Tk()
windows.minsize(width=900,height=700)
windows.config(bg=BACKGROUND_COLOR)

#CARDS
card_back=PhotoImage(file=".\\card_back.png")
card_front=PhotoImage(file=".\\card_front.png")

canvas=Canvas(width=800,height=600,bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.place(x=80,y=20)

#--------------------------- Functions ---------------------------


def english_part():
    canvas.create_image(400,290,image=card_back)
    canvas.create_text(400,200,text=f"English",font=("Comic Sans", 40, "normal"))
    english_word=df.English[choice.ind]
    canvas.create_text(400,300,text=english_word,font=("Comic Sans", 35, "bold"))

def french_part():
    canvas.create_image(400,290,image=card_front)
    canvas.create_text(400,200,text=f"French",font=("Comic Sans", 40, "normal"))
    french_word=df.French[choice.ind]
    canvas.create_text(400,300,text=french_word,font=("Comic Sans", 35, "bold"))

def count_down():
    windows.after(5000,func=english_part)

def run_program():
    choice()
    french_part()
    count_down()
    

run_program()

#--------------------------- Buttons ---------------------------

cross=PhotoImage(file=".\\wrong.png")
tick=PhotoImage(file=".\\right.png")

wrong=Button(image=cross,borderwidth=0,bg=BACKGROUND_COLOR,command=run_program)
wrong.place(x=180,y=580)
correct=Button(image=tick,borderwidth=0,bg=BACKGROUND_COLOR,command=known_words)
correct.place(x=630,y=580)



windows.mainloop()