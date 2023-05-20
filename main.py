# Imports
from turtle import Turtle, Screen

# Create screen
screen = Screen()

# Set width and height of screen
screen.setup(width=500, height=400)

# Prompt user on turtle bet
screen.textinput(title="Make your bet!", prompt="Turtles are colors of the rainbow. Enter a color: ")

# Create turtles and tell them to 'goto' their spots ;)
def create():
    # First turtle
    t1 = Turtle("turtle")
    t1.color("red")
    t1.penup()
    t1.goto(x=-230,y=-90)

create()

# Exit on click
screen.exitonclick()