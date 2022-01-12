from turtle import Turtle

SCORE_ALIGNMENT = "center"
FONT_STYLE = ("Arial", 10, "bold")


class Scoreboard(Turtle):

    def __init__(self, player_name, pos):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.goto(pos)
        self.hideturtle()
        self.write(f"{player_name}= {self.score}", move=False, align=SCORE_ALIGNMENT, font=FONT_STYLE)

    def score_up(self, player):
        self.score += 1
        self.clear()
        self.write(f"PLAYER {player} = {self.score}", move=False, align=SCORE_ALIGNMENT, font=FONT_STYLE)
