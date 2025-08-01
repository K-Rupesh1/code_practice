class QuizBrain:
    def __init__(self,q_list):
        self.question_number=0
        self.question_list=q_list
        self.score=0
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer=input(f"Q.{self.question_number}: {current_question.text} (True/False)? ")
        self.check_answer(user_answer,current_question.answer)

    def still_have_questions(self):
        if self.question_number<len(self.question_list):
            return True
        else:
            False
        
    def check_answer(self,user_answer,correct_answer):
        if user_answer.lower()==correct_answer.lower():
            self.score+=1
            print("you got right")
        else:
            print("it is wrong")
        print(f"the correct answer is:{correct_answer}")
        print(F"your current score {self.score}/{self.question_number}")
        print("\n")

