import turtle
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

df=pd.read_csv('.\\50_states.csv')
states=list(df['state'])

t=turtle.Turtle()
screen=turtle.Screen()


screen.setup(750,500)

image='blank_states_img.gif'
screen.addshape(image)
t.shape(image)

screen.tracer(0)

score=0

guessed_states=[]

while len(guessed_states)<50:

    state_name=screen.textinput(title=f"{score}/50 correct",prompt="Give a state name.")
    state_name=str(state_name)
    print(state_name)

    if state_name == 'exit' or state_name == 'Exit':
        break
    for n in states:
        if state_name.lower() == n.lower():
            guessed_states.append(n)
            xcoor=int(df['x'][df.state == n])
            ycoor=int(df['y'][df.state == n])
            t.penup()
            t.hideturtle()
            t.goto(xcoor,ycoor)
            t.write(state_name,font=("Courier",8,"bold"))
            score+=1
        

missed_states=[] 
for n in states:
    if n not in guessed_states:
        missed_states.append(n)

states_to_learn=pd.DataFrame(missed_states)
states_to_learn.to_csv('states_to_learn.csv')
print(pd.read_csv('states_to_learn.csv'))



turtle.mainloop()
