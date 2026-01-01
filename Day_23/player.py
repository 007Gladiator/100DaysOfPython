from turtle import Turtle


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.setheading(90)
        self.goto_start()


    def goto_start(self):
        self.goto(0, -280)

    def move(self):
        self.forward(20)

    def detect_collision(self, car :Turtle):
        if self.distance(car) < 20  :
            print("Game Over")
            return False
        else:
            return True

    def is_player_won(self):
        if self.ycor() > 280:
            print(f"Player Won")
            return True




