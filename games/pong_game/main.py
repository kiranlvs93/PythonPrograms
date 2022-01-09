# Player class - Create another paddle player 2
# Ball Class - Create a ball and make it move
# Detect collision with wall and bounce it
# Detect collision with paddle
# Detect when paddles misses the ball - Game over
# Score class to keep track of the scores of both the players
import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from time import sleep
# Create screen and draw a center line
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG PONG")
screen.tracer(0)

screen.listen()

# Player class - Create and move a paddle Player 1
right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
screen.onkey(right_paddle.move_up, "Up")
screen.onkey(right_paddle.move_down, "Down")
screen.onkey(left_paddle.move_up, "w")
screen.onkey(left_paddle.move_down, "s")

game_is_on = True
TOP_RIGHT = 45
BOTTOM_RIGHT = 270
while game_is_on:
    sleep(0.1)
    screen.update()
    ball.move(TOP_RIGHT)
    ball.detect_collision()


screen.exitonclick()
