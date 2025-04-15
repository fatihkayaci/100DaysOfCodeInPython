from turtle import Turtle, Screen
import random
tim = Turtle()
def draw_shape(num_sides):
    angle = 360/num_sides
    for i in range(num_sides):
        tim.right(angle)
        tim.forward(100)

def change_color():
    R = random.random()
    B = random.random()
    G = random.random()
    tim.color(R, G, B)

num_sides = 3
while num_sides < 10:
    change_color()
    draw_shape(num_sides)
    num_sides += 1