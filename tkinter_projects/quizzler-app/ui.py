from tkinter import *
from quiz_brain import *

THEME_COLOR = "#375362"
WHITE = "#FFFFFF"
RED = "#EE665D"
GREEN = "#32CD32"
FONT_NAME = "Arial"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz_ob = quiz_brain

        # Create a window
        self.window = Tk()
        self.window.title("Quiz App")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Configure Score
        self.score_label = Label(text=f"Score:0", bg=THEME_COLOR, fg=WHITE, font=(FONT_NAME, 10, "bold"))
        self.score_label.grid(row=0, column=1, sticky="E")

        # Configure question display
        self.canvas = Canvas(width=300, height=250, bg=WHITE)
        self.question_text = self.canvas.create_text(150, 125, text="Question??", fill=THEME_COLOR, width=280,
                                                     font=(FONT_NAME, 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50, padx=50)

        # true button
        true_image = PhotoImage(file="images/true.png")
        self.true_btn = Button(text="Correct", image=true_image, command=self.true_button_clicked)
        self.true_btn.grid(row=2, column=0, sticky="W")

        # false button
        false_image = PhotoImage(file="images/false.png")
        self.false_btn = Button(text="False", image=false_image, command=self.false_button_clicked)
        self.false_btn.grid(row=2, column=1, sticky="E")

        self.next_question()

        self.window.mainloop()

    def next_question(self):
        """
        Get the next question and display it in the question text as long as there are questions
        If the last question is reached, disable both the buttons and display that user has reached the end of quiz
        For every question, change the background to white
        :return:
        """
        self.canvas.config(bg=WHITE)
        if self.quiz_ob.still_has_questions():
            question = self.quiz_ob.next_question()
            self.canvas.itemconfig(self.question_text, text=question)
            self.score_label.configure(text=f"Score:{self.quiz_ob.score}")
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached the end of the QUIZ")
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")

    def true_button_clicked(self):
        """
        If True button is clicked, send True to check_answer method
        If the answer is correct, flash Green in question text box for a second else flash Red
        :return:
        """
        self.give_feedback(self.quiz_ob.check_answer("true"))

    def false_button_clicked(self):
        """
        If False button is clicked, send False to check_answer method
        If the answer is correct, flash Green in question text box for a second else flash Red
        :return:
        """
        self.give_feedback(self.quiz_ob.check_answer("false"))

    def give_feedback(self, result):
        """
        If the answer is correct, flash Green in question text box for a second else flash Red
        :param result:
        :return:
        """
        if result:
            self.canvas.configure(bg=GREEN)
        else:
            self.canvas.configure(bg=RED)
        self.window.after(1000, self.next_question)
