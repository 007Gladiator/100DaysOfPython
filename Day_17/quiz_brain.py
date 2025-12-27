class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question_list =question_list


    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number +=1
        user_response = input(f"Q,{self.question_number} : {current_question.text} (True/False) ?")
        self.check_answer(user_response, current_question.answer)

    def check_answer(self, user_response, correct_answer):
        if user_response.lower() == correct_answer.lower():
            print("you got it right!!")
            self.score += 1

        else:
            print("your answer is incorrect")
        print(f"Correct answer is : {correct_answer}")
        print(f"Your score is {self.score}/{self.question_number} \n")

