# Create a score board
# Detect collision with wall
# Detect collision with tail

from turtle import Screen
from snake import Snake
import time
from food import Food
from score import Score

# Screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Anaconda")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # Detect collision with food
    if snake.head.distance(food) < 15:
        # Create snake food randomly on the screen
        food.fresh_food()
        snake.extend_snake()
        score.increase_score()
    # Detect collision with walls
    if snake.detect_collision():
        score.game_over_msg()
        snake.reset_snake()

screen.exitonclick()
