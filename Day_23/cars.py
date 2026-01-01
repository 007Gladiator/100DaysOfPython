import random
from turtle import Turtle

colors = ["green", "red", "blue", "yellow", "pink", "orange", "brown", "magenta"]
active_area = [-230, 230]


class Cars(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.all_cars = []
        self.cars_speed = 10


    def create_car(self):
        random_chance = random.randint(1,4)
        if random_chance == 1:
            new_car = Turtle()
            new_car.penup()
            new_car.shape("square")
            new_car.shapesize(1, 2)
            new_car.color(random.choice(colors))
            new_car.goto(350, random.randrange(-230, 230, 30))
            new_car.move_x = 10
            self.all_cars.append(new_car)


    def move(self):
        for car in self.all_cars:
            new_x = car.xcor() - self.cars_speed
            car.goto(new_x, car.ycor())