from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Score
import time

screen = Screen()
screen.setup(800,600)
screen.bgcolor('black')
screen.title('Pong Game!')
screen.tracer(0)

score = Score()
ball = Ball()
r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))


screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    ball.right_corner()

    #collision with walls
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()
    
    #collision with right paddle
    if ball.xcor()>320 and ball.distance(r_paddle)<50 or ball.xcor()<-320 and ball.distance(l_paddle)<50:
        ball.bounce_x()

    #behind r_paddle
    if ball.xcor()>380: 
        score.l_point()
        ball.reset_pos()
    
    #behind l_paddle
    if ball.xcor()<-380:
        score.r_point()
        ball.reset_pos()
        


    










screen.exitonclick()