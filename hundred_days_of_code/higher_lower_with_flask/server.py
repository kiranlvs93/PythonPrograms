import random
from flask import Flask, render_template, request

app = Flask(__name__)

NO_TO_GUESS = 0
SCORE = 0


def generate_random_number(from_no, to_no):
    return random.randint(from_no, to_no)


def check_answer(guess, num_to_guess):
    """Checks answer against guess."""
    global SCORE
    print(f"Checking guess..{num_to_guess}-{guess}")
    if num_to_guess == guess:
        print(f"You got it!! Looks like u know mind reading. The answer was {num_to_guess}")
        SCORE += 1
        return 0
    if guess > num_to_guess:
        print("Too High")
        return 1
    if guess < num_to_guess:
        print("Too Low")
        return -1


@app.route("/")
def home_page():
    """
    Landing page for the flask app
    """
    global NO_TO_GUESS, NEW_GAME
    if NO_TO_GUESS == 0:
        NO_TO_GUESS = generate_random_number(1, 100)
    print(f"NO_TO_GUESS initialised->{NO_TO_GUESS}")
    return render_template("home_screen_template.html")


@app.route("/input", methods=["POST"])
def read_input():
    input_value = int(request.form["input"])
    print(f"User entered: {input_value}")
    print(f"NO_TO_GUESS is {NO_TO_GUESS}")
    result = check_answer(input_value, NO_TO_GUESS)
    if result == 0:
        return render_template("correct_guess.html")
    elif result == -1:
        return render_template("too_low.html")
    elif result == 1:
        return render_template("too_high.html")


@app.route("/newgame", methods=["POST"])
def start_new_game():
    print("Initialising NEW GAME")
    global NO_TO_GUESS
    NO_TO_GUESS = 0
    return home_page()
    # return render_template("home_screen_template.html")


@app.route("/exit", methods=["POST"])
def exit_game():
    print("EXITING CURRENT GAME")
    global NO_TO_GUESS
    NO_TO_GUESS = 0
    return render_template("exit_game.html")


if __name__ == "__main__":
    app.run(debug=True)
