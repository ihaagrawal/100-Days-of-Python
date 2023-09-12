#importing everything from turtle
from turtle import *

tim = Turtle()
tim.shape("turtle")
tim.color("coral")

#challenge 2: dashed line
def dash():
    tim.forward(5)
    tim.penup()
    tim.forward(5)
    tim.pendown()

for _ in range(25):
    dash()

screen = Screen()
screen.exitonclick()