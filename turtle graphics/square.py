from turtle import Turtle, Screen

tom = Turtle()
tom.shape("turtle")
tom.color("purple")

for _ in range(4):
    tom.forward(100)
    tom.left(90)

screen = Screen()
screen.exitonclick()