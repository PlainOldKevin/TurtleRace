# Imports
from turtle import Turtle, Screen

# Create screen
screen = Screen()

# Set width and height of screen
screen.setup(width=500, height=400)

# Prompt user on turtle bet
screen.textinput(title="Make your bet!", prompt="Turtles are colors of the rainbow. Enter a color: ")

# Create turtles and place along starting line
# Turtle colors
turtle_colors =["red", "orange", "yellow", "green", "blue", "purple"]
# Starting y position for relation to each other
starty = -90
# For loop to make 'em
for i in range(6):
    t = Turtle("turtle")
    t.color(turtle_colors[i])
    t.penup()
    # Goto here
    t.goto(-230, starty)
    # Decrese starty each loop for a line of turtles
    starty += 30


# Exit on click
screen.exitonclick()