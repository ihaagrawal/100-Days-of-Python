import turtle
from turtle import *
import random

turtle.colormode(255)

tim = Turtle()
tim.speed(100)
tim.hideturtle()

#extracted color_list in hirst_painting.py
color_list = [
    (202, 164, 110), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), 
    (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), 
    (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), 
    (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), 
    (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), 
    (168, 99, 102), (238, 240, 245)
]

#670, 360
def starting():
    tim.penup()
    tim.backward(225)
    tim.right(90)
    tim.forward(225)
    tim.left(90)
    tim.pendown()

def going_back():
    tim.penup()
    tim.left(90)
    tim.forward(50)
    tim.left(90)
    tim.forward(500)
    tim.right(180)
    tim.pendown()

starting()

for i in range(10):
    for _ in range(10):
        color_chosen = random.choice(color_list)
        tim.dot(25, color_chosen)
        tim.penup()
        tim.forward(50)
        tim.pendown()
    going_back()

screen = Screen()
screen.exitonclick()