from turtle import Screen
from players import Paddle

screen = Screen()
screen.screensize(800, 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((299, 0))
l_paddle = Paddle((-299, 0))


screen.listen()
screen.onkey(r_paddle.go_up(), "Up")
screen.onkey(r_paddle.go_down(), "Down")
screen.onkey(l_paddle.go_up(), "w")
screen.onkey(l_paddle.go_down(), "s")

game_is_on = True

while game_is_on:
    screen.update()


screen.exitonclick()
