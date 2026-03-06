"""
import colorgram
rgb_colors = []
colors = colorgram.extract('damien_hirst.jpg', 50)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b

    new_color = (r, g, b)
    rgb_colors.append(new_color)
print(rgb_colors)
"""
from turtle import Turtle, Screen
import random
turtle = Turtle()
screen = Screen()
turtle.speed('fastest')
turtle.penup()
turtle.shape("turtle")
turtle.hideturtle()
screen.colormode(255)
color_list = [(167, 155, 144), (138, 115, 96), (212, 211, 209), (155, 127, 94), (211, 216, 220), (213, 218, 215), (176, 169, 171), (212, 207, 210), (209, 197, 152), (57, 112, 134), (138, 172, 185), (145, 177, 141), (58, 127, 97), (15, 57, 80), (191, 102, 79), (110, 79, 87), (58, 40, 31), (11, 55, 46), (77, 149, 167), (6, 87, 105), (10, 99, 80), (79, 160, 137), (203, 183, 185), (203, 187, 183), (124, 38, 29), (176, 98, 107), (152, 207, 221), (36, 65, 97), (45, 34, 37), (155, 34, 39), (180, 200, 185), (75, 81, 37), (189, 190, 197), (111, 127, 148), (235, 208, 15)]
spacing = 50
start_x = -250
start_y = - 250

def draw_dot():
    turtle.dot(20,random.choice(color_list))
    turtle.forward(spacing)

for row in range(10):
    turtle.setpos(start_x, start_y + row * spacing)

    for col in range(10):
        draw_dot()


screen.exitonclick()


