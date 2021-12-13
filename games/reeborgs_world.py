"""
This is exercise solution for ReeBorg's problems
The functions with only "pass" are implemented in the website. Here they are there only for representational purpose
Link to solve the problems: https://reeborg.ca/reeborg.html
Solving this helps with understanding loops, functions, conditions, keywords and most importantly makes you think
"""


def turn_left():
    pass


def wall_on_right():
    pass


def front_is_clear():
    pass


def wall_in_front():
    pass


def left_is_clear():
    pass


def move():
    pass


def right_is_clear():
    pass


def at_goal():
    pass


def turn_right():
    turn_left()
    turn_left()
    turn_left()


def square():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_right()
    move()


def jump3():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


def jump4():
    while wall_in_front():
        turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()


# MAZE
def maze():
    while not at_goal():
        if right_is_clear():
            turn_right()
        while not front_is_clear():
            if wall_on_right():
                turn_left()
            elif wall_in_front():
                turn_right()
            elif left_is_clear():
                turn_left()
        move()


def maze1():
    while front_is_clear():
        move()
    turn_left()

    while not at_goal():
        if right_is_clear():
            turn_right()
            move()
        elif front_is_clear():
            move()
        else:
            turn_left()
