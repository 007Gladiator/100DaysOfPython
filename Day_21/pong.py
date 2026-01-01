import time
from turtle import Turtle, Screen

from Day_21.ball import Ball
from Day_21.paddle import Paddle
from Day_21.score import Score

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = Score()


screen.listen()
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")

screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")

is_game_on = True

while is_game_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    score.show_score()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()


    if ball.distance(l_paddle) < 15 or (ball.xcor() < -300 and ball.distance(l_paddle) < 50):
        print(f"l_paddle distance = {ball.distance(l_paddle)}")
        ball.bounce_x()

    if ball.xcor() > 360:
        score.update_left_score()
        ball.reset_ball()


    if ball.distance(r_paddle) < 15 or (ball.xcor() > 300 and ball.distance(r_paddle) < 50):
        print(f"r_paddle distance = {ball.distance(r_paddle)}")
        ball.bounce_x()

    if ball.xcor() < -360:
        score.update_right_score()
        ball.reset_ball()

    is_game_on = score.check_winner()
    score.show_score()
screen.exitonclick()