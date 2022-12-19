# To run: ~py golden_ratio_v3.py

'''
  Building off the last chat from golden_ratio_v3.py

  Q: Could you modify the code such that there is traditional Golden Ratio diagram spiral,
  along with right Golden Rectangles? This is the most famous visualization form of the Golden Ratio.

  A: Certainly! Here is a program that draws a traditional golden ratio spiral along with right
  golden rectangles:
    
    **code is given**
'''

# import turtle

# # Set the turtle's pen color to golden
# turtle.color('goldenrod')

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

# # Set up the window to ensure that the entire spiral is visible
# turtle.setup(1200, 1200)

# # Draw the spiral and the right Golden Rectangles
# for i in range(turns):
#     turtle.circle(length, angle)
#     turtle.left(90)
#     turtle.forward(length)
#     turtle.left(90)
#     turtle.forward(length)
#     turtle.left(180)
#     length *= phi

# # Hide the turtle
# turtle.hideturtle()

# # Keep the window open until the user closes it
# turtle.exitonclick()

'''
  Q: Make it fullscreen.

  A: Certainly! Here is a modified version of the program that opens the window in full
  screen mode:

    **code is given**
'''

import turtle
import tkinter as tk

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

# Open the window in full screen mode
root = turtle.getcanvas().winfo_toplevel()
root.attributes("-fullscreen", True)

# Draw the spiral and the right Golden Rectangles
for i in range(turns):
    turtle.circle(length, angle)
    turtle.left(90)
    turtle.forward(length)
    turtle.left(90)
    turtle.forward(length)
    turtle.left(180)
    length *= phi

# Hide the turtle
turtle.hideturtle()

# Keep the window open until the user closes it
turtle.exitonclick()

'''
  Wow... Not what I expected...

  Failed experiment at the end, but it was fun seeing the AI interpretation of the Golden Ratio.

  It appears ChatGPT does not completely recognize patterns and diagrams that naturally appeal
  to our human minds. What the AI wrote is not wrong, it's just not visually appealing or
  particularly useful for visualization purposes. Nevertheless, it was a fun experiment to learn
  more about OpenAI's ChatGPT.
'''