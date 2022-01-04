from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        # Create a snake body
        self.squares = []
        self.create_snake()
        self.head = self.squares[0]

    def create_snake(self):
        start_x_pos = 0
        start_y_pos = 0
        for _ in range(3):
            square = Turtle('square')
            square.color('white')
            square.penup()
            square.goto((start_x_pos, start_y_pos))
            start_x_pos -= 20
            self.squares.append(square)

    def move(self):
        for pos in range(len(self.squares) - 1, 0, -1):
            self.squares[pos].goto(self.squares[pos - 1].pos())
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
