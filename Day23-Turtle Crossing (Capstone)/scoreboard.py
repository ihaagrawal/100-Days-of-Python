from turtle import Turtle
class Score(Turtle):

        def __init__(self):
                super().__init__()
                self.score = 0
                self.level = 1
        
        def score_count(self):
                self.clear()
                self.penup()
                self.hideturtle()
                self.color('black')
                self.goto(-200,260)
                self.write(f"Score:{self.score}",False,align='right',font=("Comic Sans",16,"normal"))
            
        def level_count(self):
                self.clear()
                self.penup()
                self.hideturtle()
                self.color('black')
                self.goto(200,260)
                self.write(f"Level:{self.level}",False,align='left',font=("Comic Sans",16,"normal"))
                
        def score_add(self):
                self.score += 1
                self.score_count()

        def level_add(self):
                self.level += 1
                self.level_count()                
