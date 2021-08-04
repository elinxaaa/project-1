from turtle import Turtle, Screen
from random import choice

tate = Turtle()
tate.shape("turtle")

turtle_colours = ["yellow", "gold", "orange", "red", "maroon", "violet", "magenta", "purple", "navy", "blue", "skyblue", "cyan", "turquoise", "lightgreen", "green", "darkgreen", "chocolate", "brown", "black", "gray"]

for i in range(3, 11):
    angle = 360 / i
    tate.color(choice(turtle_colours))
    for _ in range(i):
        tate.forward(50)
        tate.right(angle)


screen = Screen()
screen.exitonclick()
