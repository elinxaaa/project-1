import turtle as t
from random import choice, randint

t.colormode(255)
ty = t.Turtle()
ty.speed("fastest")


def rand_colour():
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)
    rgb = (red, green, blue)
    return rgb


gap = 5

for _ in range(int(365/gap)):
    ty.color(rand_colour())
    ty.circle(75)
    ty.left(gap)

screen = t.Screen()
screen.exitonclick()
