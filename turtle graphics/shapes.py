from turtle import Turtle, Screen
from random import choice

tate = Turtle()
tate.shape("turtle")
tate.color("purple")


for i in range(3, 11):
    angle = 360 / i
    print(angle)

    for _ in range(i):
        tate.forward(50)
        tate.right(angle)


screen = Screen()
screen.exitonclick()
