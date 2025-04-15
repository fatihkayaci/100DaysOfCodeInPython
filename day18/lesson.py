from turtle import Turtle, Screen
import random
tim = Turtle()
# example 01
# tim.shape("circle")
# tim.color("red")
# for i in range(4):
#     tim.forward(100)
    # tim.right(90)

# tim.shape("arrow")
# a = 10
# for i in range(a):
#     tim.forward(a)
#     tim.penup()
#     tim.forward(a)
#     tim.pendown()
tim.speed(100)

def change_color():
    R = random.random()
    B = random.random()
    G = random.random()
    tim.color(R, G, B)

tim.setheading(5)
while tim.heading() != 0:
    change_color()
    tim.circle(100)
    tim.setheading(tim.heading() + 5)

screen = Screen()
screen.exitonclick()