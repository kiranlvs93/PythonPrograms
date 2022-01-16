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
        """
        Update the score board
        :return:
        """
        self.clear()
        self.write(f"LEVEL: {self.level}", move=False, align="center", font=FONT)

    def increment_level(self):
        """
        Increment the level by 1
        :return:
        """
        self.level += 1

    def display_message(self, message):
        """
        Display a message in the center of the screen
        :param message:
        :return:
        """
        print(message)
        self.goto((0, 0))
        self.clear()
        self.write(message, align="center", font=FONT)
        time.sleep(3)
        self.goto(POSITION)
        self.update_scoreboard()
        if message == "LEVEL UP":
            increase_move_distance()
