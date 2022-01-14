from turtle import Turtle
import time

SCORE_ALIGNMENT = "center"
FONT_STYLE = ("Arial", 14, "normal")
FONT_GAME_OVER = ("Arial", 30, "normal")
HIGH_SCORE_FILE_PATH = "HIGH_SCORE.txt"


def get_high_score():
    with open(HIGH_SCORE_FILE_PATH) as file:
        return int(file.read())


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = get_high_score()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update_score_board()

    def update_score_board(self):
        self.clear()
        self.goto(0, 280)
        self.write(f"SCORE = {self.score} \tHIGH SCORE = {self.high_score}", move=False,
                   align=SCORE_ALIGNMENT, font=FONT_STYLE)

    def increase_score(self):
        self.score += 1
        self.update_score_board()

    def game_over_msg(self):
        self.clear()
        self.goto(0, 0)
        self.write("GAME OVER", move=False, align=SCORE_ALIGNMENT, font=FONT_STYLE)
        time.sleep(2)
        self.update_high_score()
        # self.high_score = max(self.score, self.high_score)
        self.score = 0
        self.update_score_board()

    def update_high_score(self):
        self.high_score = max(self.score, self.high_score)
        with open(HIGH_SCORE_FILE_PATH, "w") as file:
            file.write(str(self.high_score))
