from quiz_brain import QuizBrain
from utilities.ascii_art import quiz as logo

print(logo)
quiz = QuizBrain()
quiz.frame_questions()

while quiz.still_has_questions():
    quiz.next_question()

print("***************************************************************************************")
print("***************************************************************************************")
print(f"You've completed the quiz.\nYour final score is: {quiz.score}/{len(quiz.questions)}")
print("***************************************************************************************")
print("***************************************************************************************")
