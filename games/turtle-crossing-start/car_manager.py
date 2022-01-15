import random
import time
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
WEST_DIR = 180
START_XPOS = 320


def create_car(start_xpos, start_ypos):
    car = Turtle("square")
    car.penup()
    car.setheading(WEST_DIR)
    car.color(random.choice(COLORS))
    car.shapesize(stretch_len=2, stretch_wid=1)
    car.goto(start_xpos, start_ypos)
    return car


def increase_move_distance():
    global STARTING_MOVE_DISTANCE
    STARTING_MOVE_DISTANCE = STARTING_MOVE_DISTANCE+MOVE_INCREMENT


class CarManager:
    def __init__(self, no_of_cars):
        super().__init__()
        self.car_list = []
        self.create_first_batch_of_cars(no_of_cars)

    def create_first_batch_of_cars(self, no_of_cars):
        for _ in range(no_of_cars):
            start_xpos = random.randrange(-START_XPOS, START_XPOS, 30)
            start_ypos = random.randrange(-240, 250, 10)
            car = create_car(start_xpos, start_ypos)
            self.car_list.append(car)

    def move_cars(self):
        for car in self.car_list:
            car.forward(STARTING_MOVE_DISTANCE)

    def generate_new_car(self):
        start_ypos = random.randrange(-240, 250, 10)
        car = create_car(START_XPOS, start_ypos)
        self.car_list.append(car)
        car.forward(STARTING_MOVE_DISTANCE)
