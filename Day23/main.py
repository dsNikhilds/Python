import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

FINISH_LINE = 280
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
scoreboard = Scoreboard()
player = Player()
carr = CarManager()

screen.listen()
screen.onkey(player.move, "Up")



game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    carr.cars()
    carr.move_cars()

    if player.ycor() > FINISH_LINE:
        player.restart()
        scoreboard.levelup()
        carr.car_speed_levelup()

    for car in carr.car_list:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.gameover()

screen.exitonclick()