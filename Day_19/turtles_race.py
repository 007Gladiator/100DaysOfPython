import random
from turtle import Turtle, Screen

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will the race? Enter a color")
colors = ["red", "blue", "green", "black", "brown", "magenta"]

no_of_turtles = 6
turtles = []
start_x = -230
start_y = -100
for i in range(5):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(x=start_x, y=start_y)
    start_y += 50
    new_turtle.speed('fast')
    turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"you have won! The {winning_color} is the the winner")
            else:
                print(f"you have lost! The {winning_color} is the the winner")
            break

        rand_distance = random.randint(-5, 15)
        rand_angle = random.randint(-45, 45)
        turtle.setheading(rand_angle)
        turtle.forward(rand_distance)
screen.exitonclick()
