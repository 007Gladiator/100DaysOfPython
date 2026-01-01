from turtle import Turtle

FONT = ("Courier", 30, "normal")

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("black")
        self.level = 1

    def show_score(self):
        self.clear()
        self.goto(-200, 280)
        self.write(f"Level : {self.level}", align="center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over", align="center", font=FONT)
