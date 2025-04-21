import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
carmanager = CarManager()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(player.player_move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    carmanager.move_car()
    carmanager.create_car()
    for car in carmanager.all_cars:
        if player.distance(car) <= 30:
            scoreboard.game_over()
            game_is_on = False

    if player.is_at_finish_line():
        player.go_to_start()
        carmanager.level_up()
        scoreboard.level_up()

    screen.update()

screen.exitonclick()