import random

# ASCII images for rock/paper/scissors gestures
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choices = [rock, paper, scissors]


def begin():
    """
    Beginning of the game to take number of rounds the user wants to play
    :return:
    """
    no_rounds = 1

    try:
        no_rounds = int(input("How many rounds of game do you want to play??"))
    except ValueError:
        print("Enter a number only. Text isn't valid input")
        exit(0)

    if no_rounds <= 0:
        print("Enter a number greater than 0")
        exit(0)
    return no_rounds


def play_game(rounds):
    """
    Game in action. Rules are as below
    Rock wins against scissors
    Scissors win against paper
    Paper wins against rock
    :param rounds:
    :return:
    """
    played = 0
    user_win = 0
    draw_match = 0
    for i in range(1, rounds + 1):
        print(f"*********************ROUND {i}*********************")
        computer_choice = random.randint(0, 2)
        user_choice = input("Type 0 for ROCK, 1 for PAPER or 2 for SCISSORS or quit to end game::")
        if user_choice == "quit" and played < rounds:
            confirmation = input(f"You committed to play {rounds} rounds but played only {played} rounds. "
                                 f"Are you sure you want to quit? Type y to confirm or enter choice to continue::")
            user_choice = confirmation
            if confirmation == 'y':
                print("Well played. Wish to see you again. Ciao!!")
                break
        played += 1
        user_choice = int(user_choice)
        # If user enter a num>2 or num<0 its invalid
        if user_choice < 0 or user_choice > 2:
            print("Enter number between 0 and 2 only. Computer is awarded 1 point for invalid input.")
        else:
            print("You chose:\n", choices[user_choice])
            print("Computer chose:\n", choices[computer_choice])

            if user_choice == computer_choice:
                print("MATCH DRAW")
                draw_match += 1
            elif user_choice == 0:
                if computer_choice == 1:
                    print("You LOSE")
                else:
                    print("You WIN")
                    user_win += 1
            elif user_choice == 1:
                if computer_choice == 2:
                    print("You LOSE")
                else:
                    print("You WIN")
                    user_win += 1
            elif user_choice == 2:
                if computer_choice == 0:
                    print("You LOSE")
                else:
                    print("You WIN")
                    user_win += 1
    return played, user_win, draw_match


def result(played, user_win, draw):
    """
    Display the results
    :param played: 
    :param user_win: 
    :param draw: 
    :return: 
    """
    computer_wins = played - user_win - draw
    print("-----------------------RESULTS ARE OUT---------------------------")
    print("Total games played::", played)
    print("Games you won::", user_win)
    print("Games computer won::", computer_wins)

    if user_win == computer_wins:
        print("You are at par with computer. MATCH DRAW")
    elif user_win > computer_wins:
        print(f"You WON against computer with a difference of score {user_win - computer_wins}")
    else:
        print(f"You LOST against computer with a difference of score {computer_wins - user_win}")
    print("-----------------------------------------------------------------")


if __name__ == '__main__':
    no_of_rounds = begin()
    played_rounds, user_wins, draw_matches = play_game(no_of_rounds)
    result(played_rounds, user_wins, draw_matches)
