from tkinter import *
from quiz_brain import *

THEME_COLOR = "#375362"
WHITE = "#FFFFFF"
FONT_NAME = "Arial"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz_ob = quiz_brain
        self.window = Tk()
        self.window.title("Quiz App")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Configure Score
        self.score = 0
        self.score_label = Label(text=f"Score:{self.score}", bg=THEME_COLOR, fg=WHITE, font=(FONT_NAME, 10, "bold"))
        self.score_label.grid(row=0, column=1, sticky="E")

        # Configure entry box
        self.canvas = Canvas(width=300, height=250, bg=WHITE)
        self.question_text = self.canvas.create_text(150, 125, text="Question??", fill=THEME_COLOR, width=280,
                                                     font=(FONT_NAME, 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50, padx=50)

        # true button
        true_image = PhotoImage(file="images/true.png")
        self.correct_btn = Button(text="Correct", image=true_image)
        self.correct_btn.grid(row=2, column=0, sticky="W")

        # false button
        false_image = PhotoImage(file="images/false.png")
        self.false_btn = Button(text="False", image=false_image)
        self.false_btn.grid(row=2, column=1, sticky="E")

        self.next_question()

        self.window.mainloop()

    def next_question(self):
        question = self.quiz_ob.next_question()
        self.canvas.itemconfig(self.question_text, text=question)
