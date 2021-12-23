from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from utilities.ascii_art import quiz as logo

print(logo)
question_bank = []
for data in question_data:
    question_bank.append(Question(data["text"], data["answer"]))

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
print("")
print(f"You've completed the quiz.\nYour final score is: {quiz.score}/{len(question_bank)}")
