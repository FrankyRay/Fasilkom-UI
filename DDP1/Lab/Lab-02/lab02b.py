## Author: Franky Raymarcell Sinaga
## NPM: 23xxxxxxxx
## File name: lab02b.py
## Using turtle to draw regular polygons
## Prompt user for the number of sides and the color components (r,g,b)

import turtle

# Configure Turtle Interface
turtle.shape('turtle')
turtle.title('Lab 02')

# Move the turtle
turtle.penup()
turtle.back(250)
turtle.pendown()

# Get the number of side from user
n = int(turtle.textinput("Lab 02", "The number of sides: "))

# Draw the n-side polygon uing for-loop
total_length = 100 * 4
for _ in range(n):
    side = total_length / n
    turtle.forward(side)
    turtle.left(360 / n)

# Get the color value (RGB)
red = float(turtle.textinput("Lab 02", "The red color component [between 0 and 1]: "))
green = float(turtle.textinput("Lab 02", "The green color component [between 0 and 1]: "))
blue = float(turtle.textinput("Lab 02", "The blue color component [between 0 and 1]: "))

# Create the color value given by the user
turtle.color(red, green, blue)

# Move the turtle into new location
turtle.penup()
turtle.forward(400)
turtle.pendown()

# Draw another n-side polygon filled with color
turtle.begin_fill()
for _ in range(n):
    side = total_length / n
    turtle.forward(side)
    turtle.left(360 / n)
turtle.end_fill()

# Make the turtle invisible
turtle.hideturtle()

# Show message for user
turtle.up()
turtle.goto(0,-100)
turtle.down()
turtle.color('blue')
turtle.write("Please click on the graphics window to exit ...",
             False, align='center', font=('Arial', 20, 'normal'))

# Exit the program when user clicked the window
turtle.exitonclick()

## THE END OF PROGRAM ##
