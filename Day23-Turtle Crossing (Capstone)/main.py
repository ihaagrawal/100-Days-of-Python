from turtle import Screen,Turtle
import time
from player import Player
from car_manager import Cars
from scoreboard import Score

t=Turtle()

screen=Screen()
screen.setup(600,600)
screen.bgcolor("white")
screen.title("Turtle Crossing")
screen.tracer(0)

player=Player()
cars=Cars()
score1=Score()
score1.score_count()
score2=Score()
score2.level_count()

screen.listen()
screen.onkey(player.move,'Up')

game_is_on=True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    cars.car_make()
    cars.car_move()

    for car in cars.all_cars:
        if player.distance(car)<20:
            t.write("GAME OVER", False, align='center',font=('Comic Sans',12,'normal'))
            game_is_on=False

        elif player.ycor()>300:
            player.goto(0,-300)
            score1.score_add()
            score2.level_add()
            cars.sp += 5

screen.exitonclick()
