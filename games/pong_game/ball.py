from turtle import Turtle

TOP_RIGHT = 45
TOP_LEFT = 135
BOTTOM_RIGHT = 225
BOTTOM_DOWN = 315
MOVE_DISTANCE = 10


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("circle")
        self.fillcolor("blue")

    def move(self, heading):
        self.setheading(heading)
        self.goto(self.xcor() + MOVE_DISTANCE, self.ycor() + MOVE_DISTANCE)

    def detect_collision(self):
        if self.xcor() > 280 and self.ycor() > 350:
            print("Upper wall bounce")
            self.move(BOTTOM_RIGHT)

        if self.xcor() > 280 and self.ycor() < -350:
            print("Lower wall bounce")
