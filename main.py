from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake Game")
screen.tracer(0)

food = Food()
snake = Snake()
scoreboard = ScoreBoard()
game_on = True
while game_on:
    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.right, "Right")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.down, "Down")

    snake.move()
    screen.update()
    time.sleep(0.1)

#collision with food
    if snake.head.distance(food) < 15:
        print("collision with food")
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

#detect collision with wall
    if snake.head.xcor() > 280 or snake.head.ycor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() < -280:
        scoreboard.game_over()
        game_on = False

#detect collison with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.game_over()
            game_on = False













screen.exitonclick()


