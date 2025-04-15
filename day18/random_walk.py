from turtle import Turtle, Screen
import random
tim = Turtle()
#random walk
def choice_direction(random_direction):
    random_number = random.randint(0,3)
    return tim.setheading(random_direction[random_number])
    
def change_color():
    R = random.random()
    B = random.random()
    G = random.random()
    tim.color(R, G, B)
    
tim.speed(9)
tim.pensize(15)

random_direction = [0, 90, 180, 270]
i = 0
while i < 100:
    change_color()
    tim.forward(30)
    choice_direction(random_direction)
    i += 1