from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level_count = 1
        self.penup()
        self.hideturtle()
        self.level()

    def level(self):
        self.goto(-200, 250)
        self.write(f"Level: {self.level_count}", align="center", font=(FONT))

    def level_up(self):
        self.level_count += 1
        self.clear()
        self.level()
        
    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=(FONT))
