from turtle import Turtle

SCORE_ALIGNMENT = "center"
FONT_STYLE = ("Arial", 8, "normal")
FONT_GAME_OVER = ("Arial", 20, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color("white")
        self.penup()
        self.goto(0, 280)
        self.hideturtle()
        self.write(f"SCORE = {self.score} High Score = {self.high_score}", move=False, align=SCORE_ALIGNMENT, font=FONT_STYLE)

    def update_score_board(self):
        self.clear()
        self.write(f"SCORE = {self.score} High Score = {self.high_score}", move=False, align=SCORE_ALIGNMENT,
                   font=FONT_STYLE)

    def increase_score(self):
        self.score += 1
        self.update_score_board()

    def game_over_msg(self):
        self.goto(0, 0)
        self.write("GAME OVER", move=False, align=SCORE_ALIGNMENT, font=FONT_GAME_OVER)
        self.high_score = max(self.score, self.high_score)
        self.update_score_board()
        self.score = 0
