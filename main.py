import time
from turtle import Screen

import player
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

turtle = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=turtle.move, key='Up')

car_counter = 0
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    car_manager.move_cars()
    car_manager.create_car()
    screen.update()

    # detect collision
    for car in car_manager.car_list:
        if turtle.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()

    # detect finish line.
    if turtle.ycor() >= player.FINISH_LINE_Y:
        turtle.player_reset()
        car_manager.level_up()
        scoreboard.next_level()




screen.exitonclick()
