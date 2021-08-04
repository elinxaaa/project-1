from turtle import Turtle, Screen
from random import choice

toe = Turtle()
turtle_colours = ["yellow", "gold", "orange", "red", "maroon", "violet", "magenta", "purple", "navy", "blue", "skyblue", "cyan", "turquoise", "lightgreen", "green", "darkgreen", "chocolate", "brown", "black", "gray"]
toe.pensize(10)
toe.speed(10)
direction = [0, 2, 3, 1]

for _ in range(100):
    toe.color(choice(turtle_colours))
    toe.forward(20)
    toe.setheading(90*choice(direction))

screen = Screen()
screen.exitonclick()
