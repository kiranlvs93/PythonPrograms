from turtle import Turtle

SCORE_ALIGNMENT = "center"
FONT_STYLE = ("Arial", 8, "normal")
FONT_GAME_OVER = ("Arial", 20, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 280)
        self.hideturtle()
        self.write("SCORE = 0", move=False, align=SCORE_ALIGNMENT, font=FONT_STYLE)

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(f"SCORE = {self.score}", move=False, align=SCORE_ALIGNMENT, font=FONT_STYLE)

    def game_over_msg(self):
        self.goto(0, 0)
        self.write("GAME OVER", move=False, align=SCORE_ALIGNMENT, font=FONT_GAME_OVER)
