# Turtle colors are available at https://cs111.wellesley.edu/labs/lab01/colors
# Trinket colors - https://trinket.io/docs/colors
from turtle import Turtle, Screen
import random
import colorgram as cg


def get_rgb_color():
    """
    Get random RGB colors. RGB ranges from 0-255
    :return:
    """
    r, g, b = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


class MyTurtle:
    def __init__(self, shape="turtle", turtle_color='blue', pen_size=2, screen_color_mode=1, speed='normal'):
        self.timmy = Turtle()
        self.timmy.shape(shape)
        self.timmy.color(turtle_color)
        self.timmy.pensize(pen_size)
        self.timmy.speed(speed)
        self.my_screen = Screen()
        self.my_screen.colormode(screen_color_mode)

    def extract_colors(self, image_name="HirstSpotPainting.jpg"):
        """
        Extract RGB colors from an image
        :return:
        """
        colors = cg.extract(image_name, 30)
        rgb_colors = []
        for color in colors:
            rgb_colors.append((color.rgb.r, color.rgb.g, color.rgb.b))
        return rgb_colors

    def draw_square(self):
        """
        Draw a square
        :return:
        """
        for _ in range(4):
            self.timmy.forward(100)
            self.timmy.left(90)

    def draw_dashed_line(self, units):
        for _ in range(units):
            self.timmy.pendown()
            self.timmy.forward(1)
            self.timmy.penup()
            self.timmy.forward(1)

    def draw_shape(self, no_of_sides):
        """
        Draw any shape given the no of sides. Angle b/w adjacent sides = 360/No of sides
        :param no_of_sides:
        :return:
        """
        self.timmy.pencolor(random.choice(["CornflowerBlue", "DarkOrchid", "IndianRed",
                                           "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]))
        for _ in range(no_of_sides):
            self.timmy.forward(100)
            self.timmy.left(360 / no_of_sides)

    def random_walk(self, speed, no_of_walks=50):
        """
        Generate random walk given the speed of the turtle and no of times it has to walk
        :param speed:
        :param no_of_walks:
        :return:
        """
        for _ in range(no_of_walks):
            self.timmy.color(random.choice(["CornflowerBlue", "DarkOrchid", "IndianRed",
                                            "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]))
            self.timmy.speed(speed)
            self.timmy.forward(30)
            self.timmy.setheading(random.choice([0, 90, 180, 270]))

    def random_walk_rgb(self, speed, no_of_walks=50):
        """
        Random walk with each step in random color
        :param speed:
        :param no_of_walks:
        :return:
        """
        for _ in range(no_of_walks):
            # RGB colors vary from 0 to 255. So choosing a random RGB color
            self.timmy.color(get_rgb_color())
            self.timmy.speed(speed)
            self.timmy.forward(30)
            self.timmy.setheading(random.choice([0, 90, 180, 270]))

    def draw_spirograph(self, radius, gap_size=50):
        """
        Draw a spirograph given the radius of the circle and the gap size b/w each circle
        :param radius:
        :param gap_size:
        :return:
        """
        for angle in range(0, 361, gap_size):
            self.timmy.color(get_rgb_color())
            self.timmy.circle(radius)
            self.timmy.setheading(angle)

    def hirst_painting(self, dot_size=20):
        """
        Hirst painting is the spotted dots painting that fetched millions of dollars on a bid
        Requirements - Canvas - 10*10 / Dot size - 20 / Spacing - 50
        :return:
        """
        # Hide the turtle because we dont want it to visible for drawing dots
        self.timmy.hideturtle()
        # move the turtle down diagonally left
        self.timmy.penup()
        self.timmy.setheading(225)
        self.timmy.forward(250)
        colors = self.extract_colors("HirstSpotPainting.jpg")
        for _ in range(10):
            self.timmy.setheading(0)
            # A row of 10 dots
            for _ in range(10):
                self.timmy.color(random.choice(colors))
                self.timmy.dot(size=dot_size)
                self.timmy.forward(50)
            self.timmy.setheading(90)
            self.timmy.forward(50)
            self.timmy.setheading(180)
            self.timmy.forward(500)

    def close_screen(self):
        """
        Close the opened screen at the end of the execution
        :return:
        """
        self.my_screen.exitonclick()
