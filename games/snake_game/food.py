from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("blue")
        self.speed("fastest")
        self.fresh_food()

    def fresh_food(self):
        """
        Create snake food randomly on the screen
        (-280,280) are boundaries of the screen within which the food has to appear.
        Its not 300 to prevent food from appearing on the edges(borders) of the screen.
        :return:
        """
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
