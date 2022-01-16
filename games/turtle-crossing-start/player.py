from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
NORTH = 90


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(NORTH)
        self.shape('turtle')

    def move_up(self):
        """
        Move up the turtle only until the finish line
        :return:
        """
        if not self.at_finish_line():
            self.forward(MOVE_DISTANCE)

    def move_down(self):
        """
        Move down the turtle only until the start line
        :return:
        """
        if self.xcor() > STARTING_POSITION[0]:
            self.backward(MOVE_DISTANCE)

    def at_finish_line(self):
        """
        Check if the player is at the finish line
        :return:
        """
        if self.distance((0, FINISH_LINE_Y)) < 10:
            print("Hurray. You reached the end unharmed!!")
            return True
        else:
            return False

    def reset_turtle(self):
        """
        Move the turtle to the starting position
        :return:
        """
        self.goto(STARTING_POSITION)
