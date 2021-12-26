from utilities.cmd_operations import clear
import requests
import pandas as pd
import random


class QuizBrain:

    def __init__(self):
        self.params = {}
        self.question_number = 0
        self.score = 0
        self.url = "https://opentdb.com/api.php"
        self.questions = pd.DataFrame()

    def get_user_choices(self):
        """
        Get the user requirements for making the quiz like no of questions, difficulty level, type of questions
        :return:
        """
        categories = {'9': '1. General Knowledge', '10': '2. Entertainment: Books', '11': '3. Entertainment: Film',
                      '12': '4. Entertainment: Music', '13': '5. Entertainment: Musicals &amp; Theatres',
                      '14': '6. Entertainment: Television', '15': '7. Entertainment: Video Games',
                      '16': '8. Entertainment: Board Games', '17': '9. Science &amp; Nature',
                      '18': '10. Science: Computers', '19': '11. Science: Mathematics', '20': '12. Mythology',
                      '21': '13. Sports', '22': '14. Geography', '23': '15. History', '24': '16. Politics',
                      '25': '17. Art', '26': '18. Celebrities', '27': '19. Animals', '28': '20. Vehicles',
                      '29': '21. Entertainment: Comics', '30': '22. Science: Gadgets',
                      '31': '23. Entertainment: Japanese Anime', '32': '24. Entertainment: Cartoon & Animations'}
        no_of_questions = int(input("How many questions would you like to answer. (Enter an integer number>0) ?"))
        print("\n".join(categories.values()))
        category_input = input(f"Which category intrigues you. Chose a number from the above list?")
        category = list(categories.keys())[
            [index for index, val in enumerate(categories.values()) if category_input in val][0]]
        difficulty = input("How hard do you want the questions to be? easy,medium,hard::")
        type_of_quest = input("What type of questions do you want? boolean/multiple::")
        print(f"Preparing questions for the choices you made as below \n No of questions - {no_of_questions}"
              f"\n Difficulty - {difficulty} \n Category - {categories.get(category)}")
        self.params = {'amount': no_of_questions, 'category': category, 'difficulty': difficulty, 'type': type_of_quest}

    def check_response(self, response):
        """
        Not all the categories have the questions. So if there are no questions, then the program will exit
        :param response:
        :return:
        """
        if response.ok and response.json()["response_code"] == 0:
            print("Request successful")
            return True
        else:
            print("Request unsuccessful. We couldn't prepare the questions. Please try again...")
            return False

    def frame_questions(self):
        """
        Getting questions from TRIVIA DB and putting them into our dataframe
        :return:
        """
        self.get_user_choices()
        print("Creating questions. Get ready to answer. Breathe in.... Breathe Out....")
        print(f"Hitting url {self.url}")
        response = requests.get(self.url, params=self.params)
        if self.check_response(response):
            resp = response.json()['results']
            self.questions = pd.DataFrame(resp)
            # Clearing the screen to display only the questions
            clear()
        else:
            exit()

    def next_question(self):
        """
        Gives the next question from the list of generated questions
        If the user input is invalid, score is reduced by 1 marks
        :return:
        """
        current_question = self.questions.loc[self.question_number]
        self.question_number += 1
        # Getting all the options and shuffling them
        options = current_question['incorrect_answers'] + [current_question['correct_answer']]
        random.shuffle(options)
        options = [str(index + 1) + '.' + option for index, option in enumerate(options)]
        print(f"Q.{self.question_number}:{current_question['question']}? \nAnswers::{' '.join(options)}:")
        user_input = input("Choose the correct option::")
        try:
            user_input = int(user_input)
        except ValueError as e:
            print("Invalid choice. Chose from the displayed numbers. Deducting 1 from your existing score")
            self.score -= 1
            user_input = "0.Invalid Choice"
        self.check_answer(options[user_input-1][2:], current_question['correct_answer'])

    def still_has_questions(self):
        """
        Checking if there are any questions left
        :return:
        """
        return self.question_number < len(self.questions)

    def check_answer(self, user_answer, correct_answer):
        """
        Check the user answer against the correct answer. If the answer is correct, then increase the score
        :param user_answer:
        :param correct_answer:
        :return:
        """
        if user_answer.lower() == correct_answer.lower():
            print("You got it right :-)")
            self.score += 1
        else:
            print("Wrong answer!!")
            print(f"The right answer is {correct_answer}.")
        print(f"Your score is {self.score}/{self.question_number}")
        print("********************************************")
