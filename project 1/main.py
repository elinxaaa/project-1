from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question["text"]
    question_ans = question["answer"]
    new_question = Question(question_text, question_ans)
    question_bank.append(new_question)

new_quiz = QuizBrain(question_bank)

while new_quiz.more_questions:
    if len(new_quiz.list) == new_quiz.number:
        break
    new_quiz.next_question()


print(f"You've completed the quiz! \nYour final score is {new_quiz.score}/{new_quiz.number}")
