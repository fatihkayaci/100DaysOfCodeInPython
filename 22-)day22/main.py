from turtle import Turtle, Screen
from paddle import Paddle
from scoreboard import Scoreboard
from ball import Ball
import time


screen = Screen()

screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("Pong")
screen.tracer(0)

scoreboard = Scoreboard()
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))


ball = Ball()

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

    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_y()
    if (ball.distance(r_paddle) < 55 or ball.distance(l_paddle) < 55) and (ball.xcor() > 330 or ball.xcor() < -330):
        ball.bounce_x()
    if ball.xcor() > 390:
        scoreboard.l_point()
        ball.restart_ball()
    if ball.xcor() < -390:
        scoreboard.r_point()
        ball.restart_ball()
    
    if scoreboard.r_score == 10 or scoreboard.l_score == 10:
        game_is_on = False

screen.exitonclick()