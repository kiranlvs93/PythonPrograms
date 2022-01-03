# Turtle colors are available at https://cs111.wellesley.edu/labs/lab01/colors
# Trinket colors - https://trinket.io/docs/colors
from turtle import Turtle, Screen
import random
import colorgram as cg
from tkinter import *


def get_rgb_color():
    """
    Get random RGB colors. RGB ranges from 0-255
    :return:
    """
    r, g, b = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


def alert_popup(title, message):
    """Generate a pop-up window for special messages."""
    root = Tk()
    root.title(title)
    w = 300  # popup window width
    h = 200  # popup window height
    sw = root.winfo_screenwidth()
    sh = root.winfo_screenheight()
    x = (sw - w) / 2
    y = (sh - h) / 2
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    m = message
    w = Label(root, text=m, width=120, height=10)
    w.pack()
    b = Button(root, text="OK", command=root.destroy, width=10)
    b.pack()
    mainloop()


class MyTurtle:
    def __init__(self, shape="turtle", turtle_color='blue', pen_size=2, screen_color_mode=1, speed='normal'):
        self.my_turtle = Turtle()
        self.my_turtle.shape(shape)
        self.my_turtle.color(turtle_color)
        self.my_turtle.pensize(pen_size)
        self.my_turtle.speed(speed)
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
            self.my_turtle.forward(100)
            self.my_turtle.left(90)

    def draw_dashed_line(self, units):
        for _ in range(units):
            self.my_turtle.pendown()
            self.my_turtle.forward(1)
            self.my_turtle.penup()
            self.my_turtle.forward(1)

    def draw_shape(self, no_of_sides):
        """
        Draw any shape given the no of sides. Angle b/w adjacent sides = 360/No of sides
        :param no_of_sides:
        :return:
        """
        self.my_turtle.pencolor(random.choice(["CornflowerBlue", "DarkOrchid", "IndianRed",
                                           "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]))
        for _ in range(no_of_sides):
            self.my_turtle.forward(100)
            self.my_turtle.left(360 / no_of_sides)

    def random_walk(self, speed, no_of_walks=50):
        """
        Generate random walk given the speed of the turtle and no of times it has to walk
        :param speed:
        :param no_of_walks:
        :return:
        """
        for _ in range(no_of_walks):
            self.my_turtle.color(random.choice(["CornflowerBlue", "DarkOrchid", "IndianRed",
                                            "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]))
            self.my_turtle.speed(speed)
            self.my_turtle.forward(30)
            self.my_turtle.setheading(random.choice([0, 90, 180, 270]))

    def random_walk_rgb(self, speed, no_of_walks=50):
        """
        Random walk with each step in random color
        :param speed:
        :param no_of_walks:
        :return:
        """
        for _ in range(no_of_walks):
            # RGB colors vary from 0 to 255. So choosing a random RGB color
            self.my_turtle.color(get_rgb_color())
            self.my_turtle.speed(speed)
            self.my_turtle.forward(30)
            self.my_turtle.setheading(random.choice([0, 90, 180, 270]))

    def draw_spirograph(self, radius, gap_size=50):
        """
        Draw a spirograph given the radius of the circle and the gap size b/w each circle
        :param radius:
        :param gap_size:
        :return:
        """
        for angle in range(0, 361, gap_size):
            self.my_turtle.color(get_rgb_color())
            self.my_turtle.circle(radius)
            self.my_turtle.setheading(angle)

    def hirst_painting(self, dot_size=20):
        """
        Hirst painting is the spotted dots painting that fetched millions of dollars on a bid
        Requirements - Canvas - 10*10 / Dot size - 20 / Spacing - 50
        :return:
        """
        # Hide the turtle because we dont want it to visible for drawing dots
        self.my_turtle.hideturtle()
        # move the turtle down diagonally left
        self.my_turtle.penup()
        self.my_turtle.setheading(225)
        self.my_turtle.forward(250)
        colors = self.extract_colors("HirstSpotPainting.jpg")
        for _ in range(10):
            self.my_turtle.setheading(0)
            # A row of 10 dots
            for _ in range(10):
                self.my_turtle.color(random.choice(colors))
                self.my_turtle.dot(size=dot_size)
                self.my_turtle.forward(50)
            self.my_turtle.setheading(90)
            self.my_turtle.forward(50)
            self.my_turtle.setheading(180)
            self.my_turtle.forward(500)

    def close_screen(self):
        """
        Close the opened screen at the end of the execution
        :return:
        """
        self.my_screen.exitonclick()

    def move_forward(self, distance):
        print("Move forwards")
        self.my_turtle.forward(distance)

    def move_backward(self):
        print("Move backwards")
        self.my_turtle.backward(10)

    def rotate_clockwise(self):
        print("Turn clockwise")
        self.my_turtle.right(10)

    def rotate_anti_clockwise(self):
        print("Turn anti-clockwise")
        self.my_turtle.left(10)

    def clear_drawing(self):
        print("Reset")
        self.my_turtle.reset()

    def pen_up(self):
        print("Pen up")
        self.my_turtle.penup()

    def pen_down(self):
        print("Pen down")
        self.my_turtle.pendown()
