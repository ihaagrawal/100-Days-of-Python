#importing everything from turtle
from turtle import *
import random

tim = Turtle()
tim.shape("arrow")
tim.color("coral")
tim.pensize(15)
tim.speed(1000)

def change_color():
     tim.color(random.random(), random.random(), random.random())

def random_walk():
     list = [90, 180, 270, 360]
     tim.forward(50)
     tim.setheading(random.choice(list))
     change_color()

for _ in range(1000):
     random_walk()

screen = Screen()
screen.exitonclick()
