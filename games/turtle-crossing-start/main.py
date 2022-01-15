# Set up the screen
# Setup the turtle. Move it to the starting position facing north
# Create cars. Moving from right of screen to left
# Detect collision with the cars
# If the turtle collides with the car, then reset the turtle
#
import time
from turtle import Screen
from player import Player
from car_manager import CarManager, create_car
from scoreboard import Scoreboard

NO_OF_CARS = 10
CAR_CREATION_DELAY = 0.1
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
cars = CarManager(NO_OF_CARS)
screen.listen()
screen.onkeypress(player.move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(CAR_CREATION_DELAY)
    screen.update()
    cars.move_cars()
    cars.generate_new_car()
    if player.at_finish_line():
        scoreboard.level_up_msg()
        scoreboard.increment_level()
        scoreboard.update_scoreboard()
        time.sleep(2)
        player.reset_turtle()



