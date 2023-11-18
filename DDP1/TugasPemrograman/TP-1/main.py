import turtle as t
from tkinter import messagebox

### Initiate turtle windows
# bricks_count = 0
t.title("Super Mario Tower Builder")
t.speed(0)
t.delay(0)

### World configuration
## Towers
# Ask the user to enter the number of towers
towers = t.numinput("World Configuration", "Enter the number of towers you want to build", 3, minval=1)
# If the input is float number, show the warning message and take the input again
while not towers.is_integer():
    messagebox.showwarning("Illegal Value", "Not an integer value\nPlease try again later")
    towers = t.numinput("World Configuration", "Enter the number of towers you want to build", 3, minval=1)
# Convert number to int
towers = int(towers)

## Layer difference
# Ask the user to enter the layer difference between each towers
layer_different = t.numinput("World Configuration", "Enter the layer differences between each towers", 5, minval=2, maxval=5)
# If the input is float number, show the warning message and take the input again
while not layer_different.is_integer():
    messagebox.showwarning("Illegal Value", "Not an integer value\nPlease try again later")
    layer_different = t.numinput("World Configuration", "Enter the layer differences between each towers", 5, minval=2, maxval=5)
# Convert number to int
layer_different = int(layer_different)

## Distance between
distance_between = 0
# Ask the user to enter the distance between each towers, if the towers is more than one
if towers > 1:
    distance_between = t.numinput("World Configuration", "Enter the distance between each tower", 2, minval=2, maxval=5)
    # If the input is float number, show the warning message and take the input again
    while not distance_between.is_integer():
        messagebox.showwarning("Illegal Value", "Not an integer value\nPlease try again later")
        distance_between = t.numinput("World Configuration", "Enter the distance between each tower", 2, minval=2, maxval=5)
    # Convert number to int
    distance_between = int(distance_between)

### Tower configuration
## Tower width
# Ask the user the width of the tower
tower_width = t.numinput("Tower Configuration", "Enter the width of the tower (per brick)", 3, maxval=10)
# If the input is float number, show the warning message and take the input again
while not tower_width.is_integer():
    messagebox.showwarning("Illegal Value", "Not an integer value\nPlease try again later")
    tower_width = t.numinput("Tower Configuration", "Enter the width of the tower (per brick)", 3, maxval=10)
# Convert number to int
tower_width = int(tower_width)

## Tower width
# Ask the user the height of the tower
tower_height = t.numinput("Tower Configuration", "Enter the height of the first tower (per brick)", 5, maxval=25)
# If the input is float number, show the warning message and take the input again
while not tower_height.is_integer():
    messagebox.showwarning("Illegal Value", "Not an integer value\nPlease try again later")
    tower_height = t.numinput("Tower Configuration", "Enter the height of the first tower (per brick)", 5, maxval=25)
# Convert number to int
tower_height = int(tower_height)

### Brick configuration
## Brick width
# Ask the user the width of the brick
brick_width = t.numinput("Brick Configuration", "Enter the width of the brick (per pixel)", 15, maxval=35)
# If the input is float number, show the warning message and take the input again
while not brick_width.is_integer():
    messagebox.showwarning("Illegal Value", "Not an integer value\nPlease try again later")
    brick_width = t.numinput("Brick Configuration", "Enter the width of the brick (per pixel)", 15, maxval=35)
# Convert number to int
brick_width = int(brick_width)

## Brick height
# Ask the user the height of the brick
brick_height = t.numinput("Brick Configuration", "Enter the height of the brick (per pixel)", 10, maxval=25)
# If the input is float number, show the warning message and take the input again
while not brick_height.is_integer():
    messagebox.showwarning("Illegal Value", "Not an integer value\nPlease try again later")
    brick_height = t.numinput("Brick Configuration", "Enter the height of the brick (per pixel)", 10, maxval=25)
# Convert number to int
brick_height = int(brick_height)

# Calculate the start position
tower_margin = brick_width * (tower_width + distance_between)
start_x = -(((tower_margin * towers) - (brick_width * distance_between)) // 2)

# Loop over each towers
for tower in range(towers):
    start_tower_x = start_x + (tower_margin * tower)
    tower_height_temp = tower_height + (layer_different * tower)
    t.color("#000000")
    t.penup()
    t.goto(start_tower_x, 0)
    t.pendown()

    for height in range(tower_height_temp + 1):
        tower_width_temp = tower_width
        color = "#CA7F65"
        t.penup()
        t.goto(start_tower_x, brick_height * height)
        t.pendown()

        if height == tower_height_temp:
            t.back(brick_width / 2)
            tower_width_temp += 1
            color = "#693424"

        for width in range(tower_width_temp):
            t.begin_fill()
            for _ in range(2):
                t.forward(brick_width)
                t.left(90)
                t.forward(brick_height)
                t.left(90)
            t.color(color)
            t.end_fill()

            # bricks_count += 1
            t.color("#000000")
            t.forward(brick_width)

        if height == tower_height_temp:
            tower_center = start_tower_x + (tower_width * brick_width) / 2

            t.penup()
            t.goto(tower_center - (brick_width * 3/4), brick_height * (height + 1) + brick_width * 3/2)
            t.pendown()

            ## Create mushroom
            # Create mushroom's body (square with side = 3/2 bricks' width)
            t.begin_fill()
            for _ in range(4):
                t.forward(brick_width * 3/2)
                t.right(90)
            t.color("#FAE69E")
            t.end_fill()

            # Create red mushroom's head (semi-circle with diameter = 2 bricks' width)
            t.color("#000000")
            t.begin_fill()
            t.back(brick_width / 4)
            t.right(90)
            t.circle(brick_width, -180)
            t.right(90)
            t.back(brick_width * 2)
            t.color("#FF0000")
            t.end_fill()

# Count the total bricks
total_bricks = towers / 2 * (2 * tower_height + (towers - 1) * layer_different) * tower_width + towers * (tower_width + 1)

# Show the output message
t.penup()
t.goto(0, -50)
t.color("#000000")
t.write(str(towers) + " tower(s) have been built with " + str(int(total_bricks)) + " bricks",
        align="center",
        font=("Arial", 16, "normal"))
t.pendown()

# Close the window when user click the interface
t.exitonclick()
