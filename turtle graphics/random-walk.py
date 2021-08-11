import turtle as t
from random import choice, randint

t.colormode(255)
toe = t.Turtle()


def rand_colour():
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint (0, 255)
    rgb = (red, green, blue)
    return rgb


toe.pensize(10)
toe.speed(10)
direction = [0, 2, 3, 1]

for _ in range(100):
    toe.color(rand_colour())
    toe.forward(20)
    toe.setheading(90*choice(direction))

screen = t.Screen()
screen.exitonclick()
