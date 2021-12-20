import random
from utilities.cmd_operations import clear
from utilities.ascii_art import guess_the_number as logo

SCORE = 0
ATTEMPTS = 0


def check_answer(guess, num_to_guess):
    """Checks answer against guess."""
    global SCORE
    if num_to_guess == guess:
        print(f"You got it!! Looks like u know mind reading. The answer was {num_to_guess}")
        SCORE += 1
        return True
    if guess > num_to_guess:
        print("Too High")
        return False
    if guess < num_to_guess:
        print("Too Low")
        return False


def higher_lower():
    """
    Higher lower game main function.
    :return:
    """
    global SCORE, ATTEMPTS
    ATTEMPTS += 1
    clear()
    num_to_guess = random.randint(1, 100)
    lost = True
    print(logo)
    print("Welcome to the NUMBER GUESSING GAME!")
    print("I'm thinking of a number between 1 and 100. Guess what it is!!")
    level = int(input("Chose a difficulty level\n1.Easy\t 2.Hard::"))
    chances = 10 if level == 1 else 5
    no_of_times_played = 0
    for i in range(chances):
        no_of_times_played += 1
        print(f"You have {chances - i} attempts remaining to guess the number")
        guess = int(input("Make a guess::"))
        if check_answer(guess, num_to_guess):
            lost = False
            break
        print("Guess Again")
    if lost and no_of_times_played == chances:
        print(f"OOPS!!! You have run out of guesses. The number was {num_to_guess}. Better luck next time!!")
    if input("Hit enter to play again or type 'quit'!!") == 'quit':
        print("Well Played. Have a good day!!")
        return
    higher_lower()


higher_lower()
print(f"You have won {SCORE} out of {ATTEMPTS} attempts")
