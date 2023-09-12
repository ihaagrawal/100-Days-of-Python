from turtle import Turtle
ALIGNMENT="center"
FONT=("Courier", 24, "normal")
class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.penup()
        self.goto(0,260)
        self.written()
        self.hideturtle()
    
    def written(self):
        self.write(f"Score:{self.score}" , align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER!", align=ALIGNMENT, font=FONT)
        
    def inc_score(self):
        self.score += 1
        self.clear()
        self.written()        