# To run: ~py golden_ratio_v2.py

'''
  Q: Could you please write a program that draws the golden ratio, in golden color, in python?

  A: Certainly! Here is a program that draws the golden ratio using the Python library turtle.
  The golden ratio is represented by the Greek letter phi (φ).

    **code is given**

  This program will draw a line with a length equal to the golden ratio (φ) times the length of 
  the first segment, and then draw a second line with a length equal to the length of the first 
  segment. The lines will be drawn in a golden color, using a triangle-shaped turtle with a pen 
  size of 5 pixels.

  I hope this helps! Let me know if you have any questions.
'''

'''
  Interestingly, ChatGPT gave me a ratio between two lines such that the condition for the Golden
  Ratio holds, instead of the iconic spiral shape attributed to the Golden Ratio.

  I need to be more specific...
'''

import turtle

# Set the turtle's pen color to golden
turtle.color('goldenrod')

# Set the turtle's speed to the maximum
turtle.speed('fastest')

# Set the turtle's shape to a triangle
turtle.shape('triangle')

# Set the turtle's pen size to 5 pixels
turtle.pensize(5)

# Set the turtle's initial position
turtle.penup()
turtle.setpos(-200, 0)
turtle.pendown()

# Set the turtle's heading to 0 degrees (pointing to the right)
turtle.setheading(0)

# Calculate the length of the first segment using the golden ratio
length = 200
phi = (1 + 5 ** 0.5) / 2
segment_length = length / phi

# Draw the first segment
turtle.forward(segment_length)

# Turn the turtle left by 144 degrees
turtle.left(144)

# Draw the second segment
turtle.forward(length)

# Hide the turtle
turtle.hideturtle()

# Keep the window open until the user closes it
turtle.exitonclick()