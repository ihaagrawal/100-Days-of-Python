from turtle import Turtle
ALIGNMENT="center"
FONT=("Courier", 24, "normal")
class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score=0
        with open('C:\\Users\\HP\\Desktop\\100days-python\\Day24-Files,Directories and Paths\\data.txt',mode='r') as data:
            self.high_score=data.read()
        self.color("white")
        self.penup()
        self.goto(0,260)
        self.written()
        self.hideturtle()

    def written(self):
        self.clear()
        self.write(f"Score:{self.score}    High Score:{self.high_score}" , align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > int(self.high_score):
            self.high_score=self.score
        with open('C:\\Users\\HP\\Desktop\\100days-python\\Day24-Files,Directories and Paths\\data.txt',mode='w') as data:
            data.write(f"{self.high_score}")
        self.score=0
        self.written()
        
    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER!", align=ALIGNMENT, font=FONT)
        
    def inc_score(self):
        self.score += 1
        self.written()
        
        
        
        
               