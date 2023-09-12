
class QuizBrain:
    def __init__(self, list):
        self.question_number = 0
        self.question_list = list
        self.score = 0
    
    def next_question(self):
        question = self.question_list[self.question_number]
        self.answer = question.answer
        self.question_number += 1
        user_answer = input(f"Q. {self.question_number}: {question.text}. True or False: ")
        self.check_answer(user_answer, question.answer)
    
    def still_has_questions(self):
        return len(self.question_list ) > self.question_number
           
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
            print(f"Your score is {self.score}/{self.question_number}")
        else:
            print("You are wrong.")
            print(f"Your score is {self.score}/{self.question_number}")
        print("\n")
            

    


