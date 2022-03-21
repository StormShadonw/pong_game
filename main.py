from turtle import Screen
import time

from Models.Ball import Ball
from Models.Paddle import Paddle
from Models.Scoreboard import Scoreboard


def create_screen():
    screen = Screen()
    screen.setup(width=800, height=600,)
    screen.bgcolor("black")
    screen.title("My pong game in Python")
    screen.tracer(0)
    return screen


screen = create_screen()
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreBoard = Scoreboard()
screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game_on = True
speed = 0.1
while game_on:
    screen.update()
    ball.move()
    time.sleep(speed)
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        speed /= 1.2
        ball.bounce_x()

    if ball.xcor() > 380:
        speed = 0.1
        ball.restart()
        scoreBoard.l_point()

    if ball.xcor() < -380:
        speed = 0.1
        ball.restart()
        scoreBoard.r_point()


screen.exitonclick()