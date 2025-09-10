from turtle import Turtle

class Paddle2(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.penup()
        self.goto(-390,0)
   
    def up(self):
        y = self.ycor()
        self.sety(y + 20)

    def down(self):
        y = self.ycor()
        self.sety(y - 20)