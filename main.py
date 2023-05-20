# Imports
from turtle import Turtle, Screen

# Create turtle and screen
t1 = Turtle()
screen = Screen()

# Set width and height of screen
screen.setup(width=500, height=400)

# Prompt user on turtle bet
screen.textinput(title="Make your bet!", prompt="Turtles are colors of the rainbow. Enter a color: ")


# Exit on click
screen.exitonclick()