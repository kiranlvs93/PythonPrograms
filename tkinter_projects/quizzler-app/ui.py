from tkinter import *

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self):
        self.window = Tk()
        self.window.title("Quiz App")

        self.window.config(padx=50, pady=50, bg=THEME_COLOR)

        self.window.mainloop()
