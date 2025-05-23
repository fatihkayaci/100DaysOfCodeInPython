from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.r_score = 0
        self.l_score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.goto(-100, 200)
        self.write(f"{self.l_score}", align="center", font=('Courier', 80, 'normal'))
        self.goto(100, 200)
        self.write(f"{self.r_score}", align="center", font=('Courier', 80, 'normal'))

    def l_point(self):
        self.l_score += 1
        self.clear()
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.penup()
        self.goto(0, 0)
        self.write("Game Over!!", align="center", font=('Courier', 24, 'normal'))