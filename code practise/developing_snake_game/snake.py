from turtle import Turtle
co_ordinates = [(0,0), (-20,0), (-40,0)]
distance = 20
Down=270 
Up=90
Right=0
Left=180 
class Snake:
    def __init__(self):
        self.all_turtles = []
        self.create_snake()
    def create_snake(self):
        for position in co_ordinates:
            self.add_segment(position) 
    def add_segment(self,position):
        new_turtle = Turtle(shape="square") 
        new_turtle.color("white")
        new_turtle.penup() 
        new_turtle.goto(position,) 
        self.all_turtles.append(new_turtle) 
    def extend(self): 
        self.add_segment(self.all_turtles[-1].position()) 
    def move(self): # Move the segments from tail to head 
        for segment_num in range(len(self.all_turtles) - 1, 0, -1): 
            new_x = self.all_turtles[segment_num - 1].xcor() 
            new_y = self.all_turtles[segment_num - 1].ycor() 
            self.all_turtles[segment_num].goto(new_x, new_y) # Move the head forward 
        self.all_turtles[0].forward(distance) 
    def up(self): 
        if self.all_turtles[0].heading()!=Down: 
            self.all_turtles[0].setheading(Up) 
    def down(self): 
        if self.all_turtles[0].heading()!=Up: 
            self.all_turtles[0].setheading(Down)
    def right(self): 
        if self.all_turtles[0].heading()!=Left: 
            self.all_turtles[0].setheading(Right) 
    def left(self): 
        if self.all_turtles[0].heading()!=Right: 
            self.all_turtles[0].setheading(Left)