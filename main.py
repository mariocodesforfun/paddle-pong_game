from turtle import Screen
from players import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
screen.screensize(800, 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((299, 0))
l_paddle = Paddle((-299, 0))
ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 288 or ball.ycor() < -288:
        ball.bounce()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 288 or ball.distance(l_paddle) < 50 or ball.xcor() < -288:
        ball.bounce_x()

    if ball.xcor() > 299:
        ball.reset_position()
        score.l_point()

    if ball.xcor() < -288:
        ball.reset_position()
        score.r_point()
