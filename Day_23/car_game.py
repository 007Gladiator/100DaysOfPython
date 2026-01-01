from time import sleep
from turtle import  Screen

from Day_23.cars import Cars
from Day_23.player import Player
from Day_23.score import Score

screen = Screen()
player = Player()
score = Score()
cars = Cars()

screen.screensize(600, 600)
screen.bgcolor("white")
screen.tracer(0)

screen.listen()
screen.onkey(player.move, "Up")

is_game_on = True
all_cars = []
while is_game_on:

    sleep(0.1)
    screen.update()
    score.show_score()
    cars.create_car()


    cars.move()
    for car in cars.all_cars:
        if car.distance(player) < 20:
            is_game_on = False
            print("Chal Nikal, game over...")
            score.game_over()

    if player.is_player_won():
        print(f"Hurray Player won!")
        score.level += 1
        player.goto_start()
        cars.cars_speed *=1.1

screen.exitonclick()