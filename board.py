from turtle import Turtle

# Constants for paddle movement and dimensions
UP = 90
DOWN = 270
FORWARD = 20

# Board class inherits from Turtle
class Board(Turtle):
    def __init__(self, x, y):
        super().__init__()

        # Initialize paddle properties
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)  # Adjust paddle dimensions
        self.goto(x, y)  # Set initial paddle position
        self.y = self.ycor()  # Store y-coordinate for movement
        self.x = self.xcor()  # Store x-coordinate for movement

    # Move the paddle up by changing its y-coordinate
    def up(self):
        if self.ycor() < 230:  # Prevent paddle from going beyond top boundary
            self.y += FORWARD  # Move paddle upward by FORWARD units
            self.goto(y=self.y, x=self.x)  # Update paddle position

    # Move the paddle down by changing its y-coordinate
    def down(self):
        if self.ycor() > -230:  # Prevent paddle from going beyond bottom boundary
            self.y -= FORWARD  # Move paddle downward by FORWARD units
            self.goto(y=self.y, x=self.x)  # Update paddle position
