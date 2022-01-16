import time
from turtle import Screen
from player import Player
from car_manager import CarManager, create_car
from scoreboard import Scoreboard

NO_OF_CARS = 10
CAR_CREATION_DELAY = 0.1

# Set up the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()

# Create a set of cars to fill the screen
cars = CarManager(NO_OF_CARS)
screen.listen()

# Use UP and DOWN arrows to move across the screen
screen.onkeypress(player.move_up, "Up")
screen.onkeypress(player.move_down, "Down")

game_is_on = True
count = 0
while game_is_on:
    time.sleep(CAR_CREATION_DELAY)
    screen.update()
    cars.move_cars()
    # Generate a new car only every 6th time the game loop runs
    if count == 3:
        cars.generate_new_car()
        count = 0
    cars.remove_car()
    if player.at_finish_line():
        scoreboard.display_message("LEVEL UP")
        scoreboard.increment_level()
        scoreboard.update_scoreboard()
        time.sleep(2)
        player.reset_turtle()
    # If the turtle collides with the car, then reset the turtle
    if cars.detect_collision(player.pos()):
        time.sleep(2)
        scoreboard.display_message("GAME OVER")
        player.reset_turtle()
    count += 1




