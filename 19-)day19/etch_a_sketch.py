from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)
    
def move_back():
    tim.back(10)
    
def turn_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)
    
def turn_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)

def clear():
    tim.clear()
screen.listen()
screen.onkey(fun=move_forwards, key="w")
screen.onkey(fun=move_back, key="s")
screen.onkey(fun=turn_right, key="d")
screen.onkey(fun=turn_left, key="a")
screen.onkey(fun=clear, key="space")
screen.exitonclick()