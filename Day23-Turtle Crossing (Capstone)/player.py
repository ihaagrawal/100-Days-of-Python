from turtle import Turtle

class Player(Turtle):

        def __init__(self):
                super().__init__()
                self.shape("turtle")
                self.color("black")
                self.penup()
                self.left(90)
                self.goto(0,-300)

        def move(self):
                self.forward(10)
        
       
                