from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for key in question_data:
    question_text = key["text"]
    question_answer = key["answer"]
    newq = Question(text = question_text, answer = question_answer)
    question_bank.append(newq)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You have finished the quiz.")
print(f"Your final score is {quiz.score}/{quiz.question_number}")