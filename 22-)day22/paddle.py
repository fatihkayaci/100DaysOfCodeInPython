from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.turtlesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.color("white")
        self.goto(position)

    def go_up(self):
        new_y = self.ycor() + 20.0
        self.setpos(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20.0
        self.setpos(self.xcor(), new_y)