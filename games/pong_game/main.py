import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

# Create screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG PONG")
screen.tracer(0)

screen.listen()

# Player class - Create and move paddles
right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
screen.onkeypress(right_paddle.move_up, "Up")
screen.onkeypress(right_paddle.move_down, "Down")
screen.onkeypress(left_paddle.move_up, "w")
screen.onkeypress(left_paddle.move_down, "s")

# Score class to keep track of the scores of both the players
left_player_score = Scoreboard("PLAYER 1", (-50, 280))
right_player_score = Scoreboard("PLAYER 2", (50, 280))

# Create a ball and make it move
ball = Ball()

game_is_on = True
while game_is_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()
    ball.detect_wall_collision()

    # Detect collision with wall and bounce it
    if (ball.distance(right_paddle) < 50 and ball.xcor() > 320) or (
            ball.distance(left_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_paddle()
    # Detect when paddles misses the ball and reset the game
    # Right paddle misses
    if ball.xcor() > 370:
        ball.reset()
        left_player_score.score_up(1)

    # Left paddle misses
    if ball.xcor() < -370:
        ball.reset()
        right_player_score.score_up(2)
screen.exitonclick()
