# lab06b_fractal.py
# *******************************************************************
# Name      : Franky Raymarcell Sinaga
# NPM       : 23xxxxxxxx
# TA Code   : XXX
# This program draws a Sierpinski fractal figure
# *******************************************************************

from turtle import *
import random

def sierpinski(length, depth):
    if depth == 1:
        colormode(255)
        r = int(random.random()*255)
        g = int(random.random()*255)
        b = int(random.random()*255)
        color(r, g, b)

    # mark position to better see recursion
    if depth > 1: dot()

    # Stamp a triangular shape on base case    
    if depth == 0: # base case
        stamp() # stamp a triangular shape

    else:
        forward(length)
        sierpinski(length/2, depth-1) # recursive call
        backward(length)
        left(120)

        forward(length)
        sierpinski(length/2, depth-1) # recursive call
        backward(length)
        left(120)
        
        forward(length)
        sierpinski(length/2, depth-1) # recursive call
        backward(length)
        left(120)

# Create a drawing screen
ts = getscreen()
ts.title("Colorful Sierpinski Fractal")

speed(0)
sierpinski(200,6)
hideturtle()
ts.exitonclick()