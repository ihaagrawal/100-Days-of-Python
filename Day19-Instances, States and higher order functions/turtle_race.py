from turtle import Turtle, Screen
import random
import turtle

turtle.colormode(255)
screen = Screen()


#to set width and height of the screen
screen.setup(width = 500, height = 500)

colors = ["red", "orange", "green", "blue", "purple", "yellow"]

all_turtles = []

y = 60
for i in range(6):
    tim = Turtle(shape="turtle")
    tim.color(colors[i])
    tim.penup()
    tim.goto(-240, y)
    y -= 30
    all_turtles.append(tim)

is_race_on = False

#for pop-up
user_bet = screen.textinput(title="Make your bet!", prompt="Which color do you bet on?")

if user_bet:
    is_race_on = True

while is_race_on:
    for turt in all_turtles:  
        if turt.xcor() > 230:
            is_race_on = False
            winner = turt.pencolor()
            if winner == user_bet:
                print(f"{winner} Won!")
                print("You've won the bet.")
            else:
                print(f"{winner} Won!") 
                print("You've lost the bet.")
        else:
            dist = random.randint(0, 10)
            turt.forward(dist)

screen.exitonclick()