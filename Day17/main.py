from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank = []
for i in question_data:
    a = i["text"]
    b = i["answer"]
    obj = Question(a,b)
    question_bank.append(obj)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("You have completed the quiz!")
print(f"Your final score is {quiz.score} / {quiz.question_number}")