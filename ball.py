from turtle import Turtle

DISTANCE = 20

# Ball class inherits from Turtle
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        
        # Initialize ball properties
        self.x = 10  # X movement distance
        self.y = 10  # Y movement distance
        self.penup()
        self.shape("circle")
        self.color("white")
        self.goto(0, 0)  # Initial position
        self.shapesize(stretch_wid=1, stretch_len=1)  # Adjust ball size
        self.move()  # Start ball movement
        self.fast = 1  # Ball's initial speed factor

    # Move the ball
    def move(self):
        self.goto((self.xcor() + self.x), (self.ycor() + self.y))

    # Bounce the ball off the top or bottom wall
    def bounce_y(self):
        self.y *= -1  # Reverse the y movement
        self.move()

    # Bounce the ball off the paddles
    def bounce_x(self):
        self.x *= -1  # Reverse the x movement
        self.move()
        if self.fast > 0.1:
            self.fast -= 0.1  # Gradually increase ball speed

    # Reset ball's position and direction
    def reset_position(self):
        self.goto(0, 0)  # Move ball to the center
        self.bounce_x()  # Reverse ball's x direction
        self.fast = 1  # Reset ball speed factor
