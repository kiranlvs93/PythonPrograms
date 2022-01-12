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
        self.x_move = MOVE_DISTANCE
        self.y_move = MOVE_DISTANCE
        self.ball_speed = 0.1

    def move(self):
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def detect_wall_collision(self):
        if self.ycor() < -285 or self.ycor() > 285:
            print("Hit wall. Bouncing off the wall")
            self.bounce_walls()

    def bounce_walls(self):
        self.y_move *= -1

    def bounce_paddle(self):
        print("Hit Paddle")
        self.ball_speed *= 0.9
        self.x_move *= -1

    def reset(self) -> None:
        print("RESETTING GAME")
        self.goto(0, 0)
        self.x_move *= -1
        self.ball_speed = 0.1
