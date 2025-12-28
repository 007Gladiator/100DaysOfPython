from turtle import Turtle, Screen
from random import random, choice, randint

timmy_turtle = Turtle()
screen = Screen()

timmy_turtle.shape('turtle')
screen.colormode(255)

timmy_turtle.pensize(1)
timmy_turtle.speed('fastest')

# colors = ['blue', 'green', 'yellow', 'orange', 'purple', 'pink', 'cyan', 'magenta', 'gold' ]
def random_color():
    r = randint(0,255)
    g = randint(0, 255)
    b = randint(0, 255)
    return (r, g, b)


################################
# step = 100
# for i in range(step):
#     if i%2 ==0:
#         timmy_turtle.pendown()
#         timmy_turtle.forward(50)
#         timmy_turtle.left(45)
#     else:
#         timmy_turtle.penup()
#         timmy_turtle.forward(50)
#         # timmy_turtle.left(45)

################################

# for j in range(10):
#     for i in range(4):
#         timmy_turtle.forward(step)
#         timmy_turtle.left(90)
#     # step += 10
#     timmy_turtle.left(45)

################################

# for i in range(3,11):
#     for j in range(i):
#         timmy_turtle.forward(100)
#         timmy_turtle.right(360/i)
#     # timmy_turtle.color()

################################

#
# for i in range(200):
#     # steps = int(random() * 100)
#     steps = 25
#     angle = int(choice([90, 180, 270, 360]))
#     timmy_turtle.color(random_color())
#     timmy_turtle.setheading(angle)
#     timmy_turtle.fd(steps)

################################

# spirograph

# radius = 130
# def draw_spirograph(size_of_gaps):
#     for i in range(int(360/ size_of_gaps)):
#         timmy_turtle.color(random_color())
#         timmy_turtle.circle(radius)
#         timmy_turtle.setheading(timmy_turtle.heading() + size_of_gaps)
#
# draw_spirograph(5)

################################


screen.exitonclick()