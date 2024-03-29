import time
from turtle import  Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width= 600 , height=600)
screen.bgcolor("black")
screen.title("my snake game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")


game_over = False

while not game_over:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
        
    if snake.head.xcor()>290 or snake.head.xcor()< -290 or snake.head.ycor()>290 or snake.head.ycor()< -290:
        scoreboard.game_over()
        game_over = True
        
        
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_over = True
            scoreboard.game_over()


screen.exitonclick()