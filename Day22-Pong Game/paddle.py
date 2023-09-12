# width = 20, height=100, x=350, y=0
from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.penup()
        self.shapesize(5,1,0)
        self.goto(position)

    def up(self):
        new_y = self.ycor() + 40
        self.goto(self.xcor(), new_y)
        
    def down(self):
        new_y = self.ycor() - 40
        self.goto(self.xcor(), new_y)
    
   
    
        