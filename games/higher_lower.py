"""
This game emulates the Higher Lower game. Everytime a user has to guess who has more followers.
If user guesses it right, then the first option is removed and the second option is compared with a new option
It goes on until the user gets a wrong guess when the final score is printed and game is aborted
"""

import os
import json

logo = """
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
"""

vs = """
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""


def clear():
    """
    Clear the console
    If you are using PyCharm, make sure the Run Configuration setting, "Emulate terminal in output console" is checked
    :return:
    """
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')


home = os.path.expanduser(os.getenv("USERPROFILE"))
data_file = fr"{home}\PycharmProjects\PythonPractice\input\higher_lower_data.json"
with open(data_file, "r") as file:
    data = json.load(file)['data']
game_status = True
counter = 0
# print(logo)

while game_status and counter < len(data) - 1:
    a, freq_a = f"{data[counter]['name']}, {data[counter]['description']}, from {data[counter]['country']}", \
                data[counter]["follower_count"]
    b, freq_b = f"{data[counter + 1]['name']}, {data[counter + 1]['description']}, from {data[counter + 1]['country']}", \
                data[counter + 1]["follower_count"]
    template1 = f"{logo}\n Compare A: {a} \n {vs} \n Against B: {b}"
    score = f"You are right. Your current score is {counter}"
    template2 = f"{logo}\n {score} \n Compare A: {a} \n {vs} \n Against B: {b}"
    print(template1 if counter == 0 else template2)
    guess = input("Who has more followers? A or B::").lower()
    if (guess == 'a' and freq_a > freq_b) or (guess == 'b' and freq_b > freq_a):
        # print(f"You are right. Your current score is {counter + 1}")
        counter += 1
        clear()
    else:
        clear()
        print(f"{logo}\n Sorry that's wrong. Your final score is {counter}")
        game_status = False
