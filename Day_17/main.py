from Day_17.data import question_data
from Day_17.quiz_brain import QuizBrain
from data import question_data
from question_model import Question

question_bank = [Question(i['text'], i['answer']) for i in question_data]
# print(question_bank)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print(f"you have completed the quiz.")
print(f"your final score is : {quiz.score} out of {quiz.question_number}")