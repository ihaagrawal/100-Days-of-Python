from turtle import Turtle, Screen

tim = Turtle()
tim.speed(100)
screen = Screen()

def move_forward():
    tim.forward(10)

screen.listen()
screen.onkey(key='space', fun=move_forward)

screen.exitonclick()