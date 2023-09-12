from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
timer_label=None
# ---------------------------- TIMER RESET ------------------------------- # 
def timer_reset():
    windows.after_cancel(timer_label)
    timer.config(text="Timer")
    timer.place(x=75,y=0)
    check.config(text="")
    canvas.itemconfig(timer_text,text="00:00")
    global reps
    reps=0
    
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    work_sec=WORK_MIN *60
    short_break_sec=SHORT_BREAK_MIN*60
    long_break_sec=LONG_BREAK_MIN*60

    if reps % 8 == 0:
        count_down(long_break_sec)
        timer.config(text="Long Break",fg=RED,bg=PINK,font=(FONT_NAME,35,"bold"))
        timer.place(x=5,y=0)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer.config(text="Short Break",fg=YELLOW,bg=PINK,font=(FONT_NAME,35,"bold"))
        timer.place(x=5,y=0)
        
    else:
        count_down(work_sec)
        timer.config(text="Work",fg=GREEN,bg=PINK,font=(FONT_NAME,35,"bold"))
        timer.place(x=95,y=0)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min=math.floor(count/60)
    count_sec=count%60
    if count_sec==0:
        count_sec = "00"
    elif count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer_label
        timer_label=windows.after(1000,count_down,count-1)
    else:
        start_timer()
        marks=""
        work_sessions=math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        check.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
windows=Tk()
windows.title("Pomodoro Timer")
windows.config(padx=100,pady=100,bg=PINK)
windows.minsize(width=500,height=500)

timer=Label(text="Timer",fg=GREEN,font=(FONT_NAME,35,"bold"),bg=PINK)
timer.place(x=75,y=0)

check=Label(fg=GREEN,font=(FONT_NAME,20,"bold"),bg=PINK)
check.place(x=85,y=300)

start=Button(text="Start",command=start_timer)
start.place(x=10,y=300)

reset=Button(text="Reset",command=timer_reset)
reset.place(x=250,y=300)

canvas=Canvas(width=200,height=224,bg=PINK,highlightthickness=0)
tomato_img=PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_img)
timer_text=canvas.create_text(100,135,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.place(x=50,y=50)

windows.mainloop()