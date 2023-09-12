#importing everything from turtle
from turtle import *
import random

tim = Turtle()
tim.shape("turtle")
tim.color("coral")
tim.penup()
tim.left(90)
tim.forward(50)
tim.pendown()
tim.right(90)

def change_color():
     tim.color(random.random(), random.random(), random.random())

def m_shape():
    angle = 360/i
    for _ in range(i):
        tim.forward(100)
        tim.right(angle)
    change_color()
   
for i in range(3, 11):
    m_shape()

screen = Screen()
screen.exitonclick()

