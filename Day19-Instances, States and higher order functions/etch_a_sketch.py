from turtle import Turtle, Screen

tim = Turtle()
tim.speed(100)
screen = Screen()

def move_forward():
    tim.forward(10)

def move_backword():
    tim.backward(10)

def rotate_clock():
    tim.right(10)

def rotate_anti():
    tim.left(10)

def clear():
    tim.clear()
    tim.reset()

screen.listen()
screen.onkey(key='w', fun=move_forward)
screen.onkey(key='s', fun=move_backword)
screen.onkey(key='d', fun=rotate_clock)
screen.onkey(key='a', fun=rotate_anti)
screen.onkey(key='c', fun=clear)

screen.exitonclick()



