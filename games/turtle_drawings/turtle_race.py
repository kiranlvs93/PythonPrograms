from my_turtle import MyTurtle, alert_popup
import random


def create_turtle(color, start_loc):
    """
    Create turtles and move them to starting position without trace
    :param color:
    :param start_loc:
    :return:
    """
    turtle = MyTurtle(turtle_color=color)
    turtle.my_turtle.penup()
    turtle.my_turtle.goto(start_loc)
    return turtle


# Screen setup
w, h = 500, 600
dummy_turtle = MyTurtle()
dummy_turtle.my_turtle.hideturtle()
screen = dummy_turtle.my_screen
screen.title("TURTLE RACE")
screen.setup(width=w, height=h)
screen.bgcolor("black")

h -= 45
turtle_colors = ["violet", "indigo", "blue", "green", "yellow", "orange", "red"]
start_x_pos = -220
# Spacing out the turtles equally along the screen height like [285, 190, 95, 0, -95, -190, -285]
start_y_pos = [h // 2 - (i * (h // 6)) for i in range(len(turtle_colors))]
all_turtles = []
winner = ""

# Create 7 turtles
for i in range(7):
    all_turtles.append(create_turtle(color=turtle_colors[i], start_loc=(start_x_pos, start_y_pos[i])))

user_bet = int(screen.numinput(title="Bet on a Turtle!!",
                               prompt="Which turtle do you want to bet on? Enter the position (1-7)", default=1,
                               minval=1,
                               maxval=len(turtle_colors)))
race_is_on = False
if 1 <= user_bet <= len(turtle_colors):
    race_is_on = True

while race_is_on:
    for turt in all_turtles:
        turt.move_forward(random.randint(0, 10))

        if turt.my_turtle.xcor() > 220:
            winner = turt.my_turtle.pencolor()
            race_is_on = False

dummy_turtle.close_screen()
alert_popup(title="Turtles Reached!!",
            message=f"Winner is {winner.upper()} at position {turtle_colors.index(winner) + 1} \n "
                    f"You guessed {turtle_colors[user_bet-1].upper()}")
alert_popup(title="Turtles Reached!!", message="Woah!! Your turtle won the race.\n🤑" if turtle_colors.index(
    winner) + 1 == int(user_bet) else "You lost!! Better luck next time")
