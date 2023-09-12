from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreboard import Score

screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor('black')
screen.title("Snake Game!")
screen.tracer(0)

snake=Snake()
food=Food()
score=Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.07)
    snake.move()
    
    #collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.inc_score()
    
    #collision with walls
    if snake.head.xcor()>290 or snake.head.xcor()<-290 or snake.head.ycor()>290 or snake.head.ycor()<-290 :
        score.game_over()
        game_is_on=False

    #collision with tail
    for seg in snake.segments[1:]:
        if snake.head.distance(seg)<10:
            score.game_over()
            game_is_on=False

screen.exitonclick()
