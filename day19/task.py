from turtle import Turtle, Screen
import random
screen = Screen()

screen.setup(width=500, height= 400)
user_bet = screen.textinput(title="Make your bet", prompt="Who will win the race? Enter a colour:").lower()

turtles = []
colors = ["red", "black", "purple", "yellow", "pink"]

def creator_turtle(i):
    turtle = Turtle(shape="turtle")
    color = random.choice(colors)
    turtle.color(color)
    colors.remove(color)
    turtle.penup()
    turtle.goto(x = -230, y = i)
    turtles.append(turtle)
is_race_on = False
if user_bet:
    is_race_on = True

i = 100
for turtle in range(5):
   creator_turtle(i)
   i -= 50

while is_race_on:
    for t in turtles:
        t.forward(random.randint(0, 5))
        if t.xcor() >= 225:
            is_race_on = False
            if t.color()[0] != user_bet:
                print(f"You Are lost. winner {t.color()[0]}")
            else:
                print(f"You are win!")

screen.listen()
screen.exitonclick()