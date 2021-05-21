from turtle import *
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Ping Pong Game")
screen.tracer(0)

paddle1 = Paddle((-350, 0))
paddle2 = Paddle((350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=paddle1.move_up)
screen.onkey(key="Down", fun=paddle1.move_down)
screen.onkey(key="w", fun=paddle2.move_up)
screen.onkey(key="s", fun=paddle2.move_down)

game_on = True

while game_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    #Wall_bouncing
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.wall_bounce()

    #Paddle miss
    if ball.xcor() > 380 or ball.xcor() < -380:
        time.sleep(1)
        ball.reset_ball()

    #scoring
    if ball.distance(paddle1) < 50 and ball.xcor() < -320:
        ball.ball_bounce()
        scoreboard.paddle1_point()

    if ball.distance(paddle2) < 50 and ball.xcor() > 320:
        ball.ball_bounce()
        scoreboard.paddle2_point()

screen.exitonclick()