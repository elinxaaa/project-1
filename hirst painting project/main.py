import random

import colorgram
import turtle as t
import random

# colours = colorgram.extract('image.jpg', 30)
# rgb_colours = []
# for colour in colours:
#     r = colour.rgb.r
#     g = colour.rgb.g
#     b = colour.rgb.b
#     new_colour = (r, g, b)
#     rgb_colours.append(new_colour)
#
# print(rgb_colours)

colour_list = [(54, 108, 149), (225, 201, 108), (134, 85, 58), (224, 141, 62), (197, 144, 171), (143, 180, 206), (137, 82, 106), (210, 90, 68), (232, 226, 194), (188, 78, 122), (69, 101, 86), (132, 183, 132), (65, 156, 86), (137, 132, 74), (48, 155, 195), (183, 191, 202), (232, 221, 225), (58, 47, 41), (47, 59, 96), (38, 44, 64), (106, 46, 54), (41, 55, 48), (12, 104, 95), (118, 125, 145), (182, 194, 199), (215, 176, 187), (223, 178, 168), (54, 45, 52)]

t.colormode(255)
tyler = t.Turtle()
tyler.speed("fastest")
tyler.penup()


def draw_circle():
    tyler.dot(20, random.choice(colour_list))


def row():
    for _ in range(10):
        draw_circle()
        tyler.forward(50)


tyler.setheading(225)
tyler.forward(300)
tyler.setheading(0)
for _ in range (10):
    row()
    tyler.setheading(90)
    tyler.forward(50)
    tyler.setheading(180)
    tyler.forward(500)
    tyler.setheading(0)

screen = t.Screen()
screen.exitonclick()
