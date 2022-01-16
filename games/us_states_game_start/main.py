import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
FONT = ("Courier", 10, "normal")

states = pd.read_csv("50_states.csv")
states['state'] = states['state'].apply(lambda x: x.lower())


def get_coordinates(inp):
    print(f"Input::{inp}")
    output = states[states.state == inp]
    return int(output.x), int(output.y)


def label_state_on_map(state_name, position):
    state_label = turtle.Turtle()
    state_label.penup()
    state_label.hideturtle()
    state_label.goto(position)
    state_label.write(state_name.title(), move=False, align="center", font=FONT)


while True:
    user_inp = screen.textinput(title="State Name", prompt="Enter a state's name").lower()
    label_state_on_map(user_inp, get_coordinates(user_inp))
