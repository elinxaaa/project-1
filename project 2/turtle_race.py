from turtle import Turtle, Screen
import random

race_status = False
screen = Screen()
screen.setup(width=500,height=400)
bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a colour: ")
colours = ["red", "orange", "yellow", "green", "blue", "purple"]
y_pos = [-70, -40, -10, 20, 50, 80]
turtles = []

for turtle_in in range(0, 6):
    t = Turtle(shape="turtle")
    t.penup()
    t.color(colours[turtle_in])
    t.goto(x=-230, y=y_pos[turtle_in])
    turtles.append(t)

if bet:
    race_status = True

while race_status:

    for turtle in turtles:
        dist = random.randint(0, 10)
        turtle.forward(dist)

    for turtle in turtles:
        if turtle.xcor() > 230:
            race_status = False
            winning_turtle = turtle.pencolor()

if winning_turtle:
    if winning_turtle.lower() == bet.lower():
        print(f"You've won! The {winning_turtle} turtle is the winner!")
    else:
        print(f"You lost. The {winning_turtle} turtle is the winner!")


screen.exitonclick()
