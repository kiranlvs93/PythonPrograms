from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270


class Paddle(Turtle):

    def __init__(self, pos):
        super().__init__()
        self.paddle = Turtle("square")
        self.paddle.penup()
        self.paddle.color("white")
        self.paddle.shape("square")
        self.paddle.shapesize(stretch_len=1, stretch_wid=5)
        self.paddle.goto(pos)

    def move_up(self):
        self.paddle.goto(self.paddle.xcor(), self.paddle.ycor() + MOVE_DISTANCE)

    def move_down(self):
        self.paddle.goto(self.paddle.xcor(), self.paddle.ycor() - MOVE_DISTANCE)
