from question_model import Question
from data import question_data 
from quiz_brain import QuizBrain
question_bank=[]
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question=Question(question_text,question_answer)
    question_bank.append(new_question)
print(question_bank)

quiz=QuizBrain(question_bank)
print(quiz.question_number)

while quiz.still_have_questions:
    quiz.next_question()
print("you have completed the game")
print(f"your final score is{quiz.score}/{quiz.question_number}")







 