from turtle import Turtle
from score import Score

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        """Create a snake body"""
        self.squares = []
        self.create_snake()
        self.head = self.squares[0]

    def create_snake(self):
        """
        Create a snake with 3 squares in white color. Head starts at (0,0) and 2 more squares behind it on X axis
        :return:
        """
        start_x_pos = 0
        start_y_pos = 0
        for _ in range(3):
            self.add_segment(start_x_pos, start_y_pos)
            start_x_pos -= 20

    def add_segment(self, start_x_pos, start_y_pos):
        square = Turtle('square')
        square.color('white')
        square.penup()
        square.goto((start_x_pos, start_y_pos))
        self.squares.append(square)

    def extend_snake(self):
        x_pos, y_pos = self.squares[-1].pos()
        self.add_segment(x_pos, y_pos)

    def move(self):
        """
        Move the head forward by MOVE_DISTANCE and the other squares follow it
        :return:
        """
        for pos in range(len(self.squares) - 1, 0, -1):
            self.squares[pos].goto(self.squares[pos - 1].pos())
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        """
        Turn the snake up (north - 90 degree) if its not facing downwards
        :return:
        """
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """
        Move the snake down (south - 270 degree) if its not facing upwards
        :return:
        """
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """
        Move the snake left (180 degree) if its not facing right
        :return:
        """
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def detect_collision(self):
        if self.head.xcor() > 290 or self.head.ycor() > 290 or self.head.xcor() < -290 or self.head.ycor() < -290:
            print("You hit the wall. GAME OVER!!")
            return True
        for square in self.squares[1:]:
            if self.head.distance(square) < 10:
                print("You hit the TAIL. GAME OVER!!")
                return True
        return False
