import time
from turtle import Turtle
from car_manager import increase_move_distance

FONT = ("Courier", 24, "normal")
POSITION = (-210, 250)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(POSITION)
        self.hideturtle()
        self.level = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"LEVEL: {self.level}", move=False, align="center", font=FONT)

    def increment_level(self):
        self.level += 1

    def level_up_msg(self):
        print("LEVEL UP")
        self.goto((0, 0))
        self.clear()
        self.write(f"LEVEL UP", align="center", font=FONT)
        increase_move_distance()
        time.sleep(3)
        self.goto(POSITION)
        self.update_scoreboard()
