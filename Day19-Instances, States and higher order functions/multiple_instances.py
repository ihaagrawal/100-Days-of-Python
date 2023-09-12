from turtle import Turtle, Screen

tim = Turtle()
bob = Turtle()

tim.shape("turtle")
bob.shape("turtle")

tim.color("green")
bob.color("yellow")
bob.forward(100)

screen = Screen()
screen.exitonclick()