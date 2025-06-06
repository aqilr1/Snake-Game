import time
from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Snake Game")
screen.tracer(0)


snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(key='w', fun=snake.up)
screen.onkey(key='s', fun=snake.down)
screen.onkey(key='a', fun=snake.left)
screen.onkey(key='d', fun=snake.right)

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    #Detect collision with food
    if snake.head.distance(food) < 15:
        snake.add_segment()
        food.refresh_location()
        scoreboard.increase_score()

    #Detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        scoreboard.end_game()

    #Detect collision with tail
    for segment in snake.snake_segments[1:]:
        if snake.head.distance(segment)<15:
            game_is_on = False
            scoreboard.end_game()


screen.exitonclick()