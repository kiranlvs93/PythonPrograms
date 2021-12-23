from typing import List


class QuizBrain:

    def __init__(self, questions: List):
        self.category = ""
        self.no_of_questions = 0
        self.question_number = 0
        self.questions_list = questions
        self.score = 0

    def frame_questions(self):
        URL = "https://opentdb.com/api.php?amount={no_of_questions}&category=18&difficulty=easy&type=boolean"
        categories = {"9": "General Knowledge", "10": "Entertainment: Books", "11": "Entertainment: Film",
                      "12": "Entertainment: Music", "13": "Entertainment: Musicals &amp; Theatres",
                      "14": "Entertainment: Television", "15": "Entertainment: Video Games",
                      "16": "Entertainment: Board Games", "17": "Science &amp; Nature",
                      "18": "Science: Computers", "19": "Science: Mathematics", "20": "Mythology",
                      "21": "Sports", "22": "Geography", "23": "History", "24": "Politics",
                      "25": "Art", "26": "Celebrities", "27": "Animals", "28": "Vehicles",
                      "29": "Entertainment: Comics", "30": "Science: Gadgets",
                      "31": "Entertainment: Japanese Anime", "32": "Entertainment: Cartoon & Animations"}
        self.no_of_questions = int(input("How many questions would you like to answer. (Enter an integer number>0) ?"))
        print("\n".join(k + "." + v for k, v in categories.items()))
        self.category = int(input(f"Which category intrigues you. Chose a number from above list?"))
        self.difficulty = input("How hard do you want to the questions to be? easy,medium,hard")
        self.questions_type = input("Question type: true/false or multiple choice")

    def next_question(self):
        current_question = self.questions_list[self.question_number]
        self.question_number += 1
        user_input = input(f"Q.{self.question_number}:{current_question.text} (true/false):")
        self.check_answer(user_input.lower(), current_question.answer.lower())

    def still_has_questions(self):
        return self.question_number < len(self.questions_list)

    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer:
            print("You got it right :-)")
            self.score += 1
        else:
            print("Wrong answer!!")
            print(f"The right answer is {correct_answer}.")
        print(f"Your score is {self.score}/{self.question_number}")
        print("********************************************")
