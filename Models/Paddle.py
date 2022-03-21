from turtle import Turtle
POSITIONS = [(350, -40), (350, -20), (350, 0), (350, 20), (350, 40)]


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.turtles = []
        self.positions = []
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid= 5, stretch_len= 1)
        self.goto(position)

    def up(self):
        if self.xcor() < 0:
            self.goto(-350, self.ycor() + 20)
        else:
            self.goto(350, self.ycor() + 20)


    def down(self):
        if self.xcor() < 0:
            self.goto(-350, self.ycor() - 20)
        else:
            self.goto(350, self.ycor() - 20)
