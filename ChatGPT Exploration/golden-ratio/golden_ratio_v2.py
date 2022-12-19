# To run: ~py golden_ratio_v2.py

'''
  Building off the last chat from golden_ratio_v1.py

  Q: Could you please write a program that draws the golden ratio spiral, in golden color, in python?

  A: Certainly! Here is a program that draws a golden ratio spiral using the Python library turtle.
  The golden ratio is represented by the Greek letter phi (φ).

    **code is given**

  This program will draw a spiral by turning left by an angle that is determined by the golden ratio (φ)
  at each iteration, and increasing the length of the line drawn at each iteration by a factor of φ.
  The spiral will be drawn in a golden color, using a turtle with a pen size of 1 pixel.

  I hope this helps! Let me know if you have any questions.
'''

# # import turtle

# # Set the turtle's pen color to golden
# # turtle.color('goldenrod')

# # Set the turtle's speed to the maximum
# turtle.speed('fastest')

# # Set the turtle's pen size to 1 pixel
# turtle.pensize(1)

# # Set the turtle's initial position
# turtle.penup()
# turtle.setpos(0, 0)
# turtle.pendown()

# # Set the turtle's heading to 0 degrees (pointing to the right)
# turtle.setheading(0)

# # Set the length of the first segment
# length = 200

# # Set the number of turns
# turns = 10

# # Calculate the angle to turn at each iteration using the golden ratio
# phi = (1 + 5 ** 0.5) / 2
# angle = 360 * phi

# # Draw the spiral
# for i in range(turns):
#     turtle.forward(length)
#     turtle.left(angle)
#     length *= phi

# # Hide the turtle
# turtle.hideturtle()

# # Keep the window open until the user closes it
# turtle.exitonclick()

'''
  The code initially given was out of bounds.

  Q: The drawing is out of bounds. Could you add an extra setup step to make sure everything can be seen?

  A: Certainly! Here is a modified version of the program that includes a setup step to ensure that the
  entire spiral is visible:

    **code is given**

  The turtle.setup() function sets the size of the window that the turtle will draw in. In this case, 
  the window is set to 1200x1200 pixels, which should be large enough to accommodate the entire spiral.

  I hope this helps! Let me know if you have any questions.
'''

'''
  Much better. I still want to see a version with a curve, instead of lines agreeing with the
  Golden Ratio.
'''

import turtle

# Set the turtle's pen color to golden
turtle.color('goldenrod')

# Set the turtle's speed to the maximum
turtle.speed('fastest')

# Set the turtle's pen size to 1 pixel
turtle.pensize(1)

# Set the turtle's initial position
turtle.penup()
turtle.setpos(0, 0)
turtle.pendown()

# Set the turtle's heading to 0 degrees (pointing to the right)
turtle.setheading(0)

# Set the length of the first segment
length = 200

# Set the number of turns
turns = 10

# Calculate the angle to turn at each iteration using the golden ratio
phi = (1 + 5 ** 0.5) / 2
angle = 360 * phi

# Set up the window to ensure that the entire spiral is visible
turtle.setup(1200, 1200)

# Draw the spiral
for i in range(turns):
    turtle.forward(length)
    turtle.left(angle)
    length *= phi

# Hide the turtle
turtle.hideturtle()

# Keep the window open until the user closes it
turtle.exitonclick()
