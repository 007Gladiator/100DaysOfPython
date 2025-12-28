import random
from turtle import Turtle, Screen

import colorgram



# colors = colorgram.extract('hirst_image2.jpg', 30)
# rgb_colors = [(color.rgb[0], color.rgb[1], color.rgb[2])  for color in colors]
# print(rgb_colors)

rgb_colors = [ (249, 228, 17), (213, 13, 9), (198, 12, 35), (231, 228, 5), (197, 69, 20), (33, 90, 188), (43, 212, 71), (234, 148, 40), (33, 30, 152), (16, 22, 55), (66, 9, 49), (244, 39, 149), (65, 202, 229), (14, 205, 222), (63, 21, 10), (224, 19, 111), (229, 165, 8), (15, 154, 22), (245, 58, 16), (98, 75, 9), (248, 11, 9), (222, 140, 203), (68, 240, 161), (10, 97, 62), (5, 38, 33), (68, 219, 155)]

tim = Turtle()
screen = Screen()
screen.colormode(255)
# tim.dot(10, 'red')
# tim.fd(50)
step_size = 50
tim.setheading(225)
tim.penup()
tim.hideturtle()
tim.forward(300)
tim.setheading(0)
tim.pendown()

for j in range(10):

    for i in range(10):
        tim.dot(step_size/2, random.choice(rgb_colors))
        tim.penup()
        if i < 9:
            tim.fd(step_size)
    if j%2 ==0:
        tim.left(90)
        tim.fd(step_size)
        tim.left(90)
    else:
        tim.right(90)
        tim.fd(step_size)
        tim.right(90)


screen.exitonclick()
