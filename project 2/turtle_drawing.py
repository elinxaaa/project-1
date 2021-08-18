from turtle import Turtle, Screen

tory = Turtle()
screen = Screen()


def forwards():
    tory.forward(10)


def backwards():
    tory.back(10)


def counter_clock():
    tory.left(15)


def clockwise():
    tory.right(15)


def clean():
    tory.clear()
    tory.penup()
    tory.home()
    tory.pendown()

screen.listen()


screen.onkey(key="w", fun=forwards)
screen.onkey(key="s", fun=backwards)
screen.onkey(key="a", fun=counter_clock)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="c", fun=clean)
screen.exitonclick()
