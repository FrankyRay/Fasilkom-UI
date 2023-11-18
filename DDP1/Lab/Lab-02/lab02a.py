## Author: Franky Raymarcell Sinaga
## NPM: 23xxxxxxxx
## File name: lab02a.py
## Using Turtle to draw a hexagon
import turtle

# Start up a Turtle Graphics window with a green turtle
turtle.color('green')
# Put its pen down so all movement will show as a green line
turtle.pendown()

# Create hexagon by move forward by 100 and rotate 60 degrees 6 times
for _ in range(6):
    turtle.forward(100)
    turtle.right(60)

# Make the turtle invisible
turtle.hideturtle()
# Exit the program when user clicked the window
turtle.exitonclick()

## THE END OF PROGRAM ##
