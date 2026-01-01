from asyncore import write
from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = 0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0, 270)
        self.load_highscore()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score = {self.score} High Score = {self.highscore}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)

    def reset(self):
        print(f"in reset method")
        if self.score > self.highscore:
            print("update higscore")
            self.highscore = self.score
            self.update_highscore()
        print(f'reset score to zero')
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score +=1
        self.clear()
        self.update_scoreboard()


    def load_highscore(self):
        with open('data.txt', 'r') as highscore:
            # print(highscore.read())
            self.highscore = int(highscore.read())


    def update_highscore(self):
        with open('data.txt', 'w') as highscore:
            highscore.write(str(self.highscore))
