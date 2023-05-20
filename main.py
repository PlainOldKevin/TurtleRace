# Imports
from turtle import Turtle, Screen
import random as r

# Create screen and title
screen = Screen()
screen.title("Turtle Race")

# Set width and height of screen
screen.setup(width=500, height=400)

# Bool for race beginning
race_start = False

# Prompt user on turtle bet
user_bet = screen.textinput(title="Make your bet!", prompt="Turtles are colors of the rainbow. Enter a color: ")

# Create turtles and place along starting line
# Turtle colors
turtle_colors =["red", "orange", "yellow", "green", "blue", "purple"]
# Starting y position for relation to each other
starty = -75
# List to hold the turtles
all_turtles = []
# For loop to make 'em
for i in range(6):
    t = Turtle("turtle")
    t.color(turtle_colors[i])
    t.penup()
    # Goto here
    t.goto(-230, starty)
    # Decrese starty each loop for a line of turtles
    starty += 30
    # Append list to store turtles
    all_turtles.append(t)

# Check user input to start race
if user_bet:
    race_start = True

# Start race
while race_start:
    # Loop thru list and move each turtle a random amount
    for turtle in all_turtles:
        move = r.randint(0, 10)
        turtle.forward(move)

# Exit on click
screen.exitonclick()