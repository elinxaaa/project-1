from turtle import Turtle
MOVE_DIST = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.body = []
        self.create_snake()
        self.head = self.body[0]

    def create_snake(self):
        for x in range(0, 3):
            t = Turtle("square")
            t.color("white")
            t.penup()
            t.goto(x=0 - 20 * x, y=0)
            self.body.append(t)

    def move(self):
        for seg in range(len(self.body) - 1, 0, -1):
            coordx = self.body[seg - 1].xcor()
            coordy = self.body[seg - 1].ycor()
            self.body[seg].goto(coordx, coordy)
        self.head.forward(MOVE_DIST)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)





