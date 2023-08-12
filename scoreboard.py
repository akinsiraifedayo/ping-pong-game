from turtle import Turtle

# Constants for scoreboard positioning and formatting
L_SCORE_POSITION = (-100, 200)  # Position for left player's score
R_SCORE_POSITION = (100, 200)   # Position for right player's score
ALIGNMENT = "center"            # Text alignment for score display
FONT = ("Courier", 80, "normal")  # Font style for score display

# Scoreboard class inherits from Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()

        # Initialize scores and display settings
        self.l_score = 0  # Left player's score
        self.r_score = 0  # Right player's score
        self.color("white")
        self.penup()
        self.update_score()  # Display initial scores
        self.hideturtle()     # Hide the turtle cursor

    # Update and display the scores on the screen
    def update_score(self):
        self.clear()  # Clear previous score display
        self.goto(R_SCORE_POSITION)  # Position for right player's score
        self.write(arg=f"{self.l_score}", align=ALIGNMENT, move=True, font=FONT)
        self.goto(L_SCORE_POSITION)  # Position for left player's score
        self.write(arg=f"{self.r_score}", align=ALIGNMENT, move=True, font=FONT)

    # Increment the left player's score and update the display
    def l_wins(self):
        self.l_score += 1  # Increment left player's score
        self.update_score()  # Update the score display

    # Increment the right player's score and update the display
    def r_wins(self):
        self.r_score += 1  # Increment right player's score
        self.update_score()  # Update the score display
