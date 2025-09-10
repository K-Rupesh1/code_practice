from turtle import Screen
from paddle import Paddle
from paddle2 import Paddle2
from ball import Ball
from score_board import Score_board
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Welcome to the PONG game")
screen.listen()
screen.tracer(0)

paddle = Paddle()
paddle2 = Paddle2()
ball = Ball()
score_board = Score_board()

screen.onkey(paddle.up, "Up")
screen.onkey(paddle.down, "Down")
screen.onkey(paddle2.up, "w")
screen.onkey(paddle2.down, "s")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # bounce off top or bottom wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # bounce off paddles
    if (ball.distance(paddle) < 50 and ball.xcor() > 320) or \
       (ball.distance(paddle2) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    # right wall miss
    if ball.xcor() > 380:
        ball.bounce_reposition()
        score_board.increment_paddle_score()
        time.sleep(1)

    # left wall miss
    if ball.xcor() < -380:
        ball.bounce_reposition()
        score_board.increment_paddle_score2()
        time.sleep(1)

screen.exitonclick()
