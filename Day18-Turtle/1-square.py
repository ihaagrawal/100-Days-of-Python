#importing everything from turtle
from turtle import *

tim = Turtle()
tim.shape("turtle")
tim.color("coral")

#challenge 1: drawing a square
def square():
    tim.forward(100)
    tim.right(90)

for _ in range(4):
    square()


screen = Screen()
screen.exitonclick()