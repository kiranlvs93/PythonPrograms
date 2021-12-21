from question_model import Question
from data import question_data

question_bank = []
for data in question_data:
    question_bank.append(Question(data["text"], data["answer"]))

print(len(question_bank))
print(question_bank[0].text)
print(question_bank[0].answer)
