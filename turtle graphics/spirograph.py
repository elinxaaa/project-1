import turtle as t
from random import choice, randint

t.colormode(255)
ty = t.Turtle()

def rand_colour():
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)
    rgb = (red, green, blue)
    return rgb

