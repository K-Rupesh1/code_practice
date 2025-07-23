'''from quiz_brain import QuizBrain
from data import question_data
from question_model import Question
question_bank=[]
for question in question_data:
    question_text=question["question"]
    question_answer=question["correct_answer"]
    new_question=Question(question_text,question_answer)
    question_bank.append(new_question)
print(question_bank)

quiz=QuizBrain(question_bank)
print(quiz.next_question)
while quiz.still_have_questions:
    quiz.next_question()
print("you have completed the game")
print(f"your final score is{quiz.score}/{quiz.question_number}")'''


from quiz_brain import QuizBrain
from data import question_data
from question_model import Question

question_bank = []
for question in question_data["results"]:
    category = question["category"]
    question_text = question["question"]
    question_answer = question["correct_answer"]
    incorrect_answers = question["incorrect_answers"]  # ✅ fixed

    new_question = Question(category, question_text, question_answer, incorrect_answers)  # ✅ fixed
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_have_questions():
    quiz.next_question()

print("You've completed the quiz!")
print(f"Your final score is: {quiz.score}/{quiz.question_number}")



