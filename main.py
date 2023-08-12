from turtle import Screen
from board import Board
from ball import Ball
from scoreboard import Scoreboard
import time

# Create right and left paddles, ball, and scoreboard
right_paddle = Board(350, 0)
left_paddle = Board(-350, 0)
ball = Ball()
scoreboard = Scoreboard()

# Set up the screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Ping Pong Game")
screen.tracer(0)  # Turn off auto-updates
screen.listen()

# Set up key bindings for paddle movement
screen.onkey(key="Up", fun=right_paddle.up)
screen.onkey(key="Down", fun=right_paddle.down)

screen.onkey(key="w", fun=left_paddle.up)
screen.onkey(key="s", fun=left_paddle.down)

# Game loop
game_is_on = True
while game_is_on:
    time.sleep(0.1 * ball.fast)  # Slow down the ball's movement
    screen.update()  # Update the screen
    crossed_x = False

    # Check if the ball crossed the left or right boundary
    if ball.xcor() > 320 or ball.xcor() < -320:
        crossed_x = True

    # Check for collision with paddles
    if ((ball.distance(right_paddle) < 50) and crossed_x) or (ball.distance(left_paddle) < 50 and crossed_x):
        ball.bounce_x()  # Reverse ball's x-direction

    # Check for collision with top or bottom walls
    elif ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()  # Reverse ball's y-direction

    # Check if the ball crossed the right boundary (left player wins)
    elif ball.xcor() > 380:
        ball.reset_position()  # Reset ball position
        scoreboard.r_wins()  # Increment right player's score
        right_paddle.goto(350, 0)  # Reset paddles' positions
        left_paddle.goto(-350, 0)

    # Check if the ball crossed the left boundary (right player wins)
    elif ball.xcor() < -380:
        ball.reset_position()  # Reset ball position
        scoreboard.l_wins()  # Increment left player's score
        right_paddle.goto(350, 0)  # Reset paddles' positions
        left_paddle.goto(-350, 0)

    # If none of the above conditions, move the ball
    else:
        ball.move()

# Close the game window when clicking
screen.exitonclick()
