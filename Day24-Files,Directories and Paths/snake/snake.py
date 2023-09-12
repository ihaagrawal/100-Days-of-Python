from turtle import Turtle
STARTING_POS = [(0,0), (-20,0), (-40,0)]
DIST = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0   
class Snake:
    def __init__(self):
        self.segments = []
        self.draw()
        self.head=self.segments[0]

    def draw(self):
        for position in STARTING_POS:
            self.add_segments(position)
            
        
    def add_segments(self, position):
        ti=Turtle()
        ti.shape("square")
        ti.color("white")
        ti.penup()
        ti.goto(position)
        self.segments.append(ti)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.draw()
        self.head=self.segments[0]
    
    def extend(self):
        self.add_segments(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments)-1, 0, -1):
            new_x=self.segments[seg_num-1].xcor()
            new_y=self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x,new_y)
        self.head.forward(DIST)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)
        
    def down(self):
        if self.head.heading() != UP: 
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)
        
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)
        



