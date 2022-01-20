import time
import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
FONT = ("Courier", 8, "bold")

states_df = pd.read_csv("50_states.csv")
states_df['state'] = states_df['state'].apply(lambda x: x.lower())
input_box_title = "Guess The State"
correct_states = 0
states_list = list(states_df['state'])


def get_coordinates(inp):
    print(f"Input::{inp}")
    output = states_df[states_df.state == inp]
    return int(output.x), int(output.y)


def label_state_on_map(state_name, position):
    state_label = turtle.Turtle()
    state_label.penup()
    state_label.hideturtle()
    state_label.goto(position)
    state_label.write(state_name.title(), move=False, align="center", font=FONT)


game_is_on = True
while game_is_on:
    user_inp = screen.textinput(title=input_box_title, prompt="Enter a state's name").lower()
    # If the state is wrongly guessed
    if user_inp not in list(states_df['state']):
        input_box_title = "State Doesn't Exist"
    # If the state is already guessed, change the title accordingly
    if user_inp in list(states_df['state']) and user_inp not in states_list:
        input_box_title = "State already marked"
    # Label the state on the map and pop it off from the states list
    if user_inp in states_list:
        label_state_on_map(user_inp, get_coordinates(states_list.pop(states_list.index(user_inp))))
        correct_states += 1
        input_box_title = f"{correct_states}/{len(states_df['state'])} States Guessed Correctly"
    # End the game if all the states are guessed or if the user wants to exit
    if len(states_list) == 0 or user_inp == "exit":
        time.sleep(2)
        pd.DataFrame(states_list, columns=["Remaining State"]).to_csv("StatesNotGuessed.csv")
        game_is_on = False
