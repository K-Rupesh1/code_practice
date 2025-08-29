from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.penup()
        self.color("red")
        self.speed("fastest")
        self.Refresh()
    def Refresh(self):
        x_axis=random.randint(-270,270)
        y_axis=random.randint(-270,270)
        self.goto(x_axis,y_axis)
