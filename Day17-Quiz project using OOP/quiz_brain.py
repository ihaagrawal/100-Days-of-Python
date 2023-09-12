class QuizBrain:

    def __init__(self, list):
        self.question_number = 0
        self.question_list = list
        self.question_score = 0
    
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        self.user_answer = input(f"Q.{self.question_number}: {current_question.text}. True or False: ")
        self.check_answer(self.user_answer, current_question)

    def still_has_questions(self):
        return len(self.question_list) > self.question_number
    
    def check_answer(self, user_answer, current_question):
        if self.user_answer.lower() == current_question.answer.lower():
            self.question_score += 1
            print("You are right.")
            print(f"Your score is {self.question_score}/{self.question_number}.")
        else:
            print("You are wrong.")
            print(f"Your score is {self.question_score}/{self.question_number}.")




        