from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.r_score = 0
        self.l_score = 0
        self.match_point = 5


    def show_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))

        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

    def update_right_score(self):
        self.r_score += 1
        print(f"Rgith score = {self.r_score}")

    def update_left_score(self):
        self.l_score += 1
        print(f"Left score = {self.l_score}")

    def check_winner(self):
        if self.r_score >= 5:
            print(f"Right player won!!!")
            return False
        elif self.l_score >=5:
            print(f"Left player won!!!")
            return False
        else:
            return True