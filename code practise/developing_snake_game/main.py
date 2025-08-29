from turtle import Screen
import time
from snake import Snake  
from food import Food
from score_board import Score_board

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Welcome to the Snake Game")
screen.tracer(0)

snake = Snake()
food=Food()
score_board=Score_board()
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    screen.listen()
    screen.onkey(snake.up,"Up")#always we want use the first letter in this is caps
    screen.onkey(snake.down,"Down")
    screen.onkey(snake.right,"Right")
    screen.onkey(snake.left,"Left")
    #Detect collision with food
    if snake.all_turtles[0].distance(food)<15:
        food.Refresh()
        snake.extend()
        score_board.increase_score()
    
    #Detect collision with wall
    if snake.all_turtles[0].xcor()>280 or snake.all_turtles[0].xcor()<-280 or snake.all_turtles[0].ycor()>280 or snake.all_turtles[0].ycor()<-280:
        
        score_board.game_over()
        game_is_on=False
    for segment in snake.all_turtles[1:]:
        if snake.all_turtles[0].distance(segment)<10:
            game_is_on=False
            score_board.game_over()

screen.exitonclick()

