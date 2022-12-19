# To run: ~py golden_ratio_v3.py

'''
  Building off the last chat from golden_ratio_v2.py

  Q: Could you please use a curve, instead of a sequence of lines, to draw the golden ratio? 
  The result should be a spiral, curved, not straight.

  A: Certainly! Here is a program that draws a golden ratio spiral using curves instead of a
  sequence of lines:

    **code is given**

  This program draws a spiral by using the turtle.circle() function to draw a curve with a
  radius equal to the length of the current segment, and turning left by an angle that is
  determined by the golden ratio (φ) at each iteration. The spiral will be drawn in a golden
  color, using a turtle with a pen size of 1 pixel.

  I hope this helps! Let me know if you have any questions.
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

# # Draw the spiral
# for i in range(turns):
#     turtle.circle(length, angle)
#     length *= phi

# # Hide the turtle
# turtle.hideturtle()

# # Keep the window open until the user closes it
# turtle.exitonclick()

'''
  Interestingly, the window popup was showing halfway out or my screen (above).
  I tried to let ChatGPT deal with it.

  Q: The window popup seems to appear halfway above my screen. Could you fix that for me?

  A: Certainly! Here is a modified version of the program that positions the window at the center of the screen:

    **code is given**

  This program uses the turtle.window_width() and turtle.window_height() functions to get the width
  and height of the screen, and the turtle.getcanvas().winfo_toplevel() function to get the root window
  that contains the turtle canvas. The root.geometry() function is then used to position the window at
  the center of the screen.

  I hope this helps! Let me know if you have any questions.
'''

# import turtle
# import tkinter as tk

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

# # Get the screen width and height
# screen_width = turtle.window_width()
# screen_height = turtle.window_height()

# # Set up the window to ensure that the entire spiral is visible
# turtle.setup(1200, 1200)

# # Position the window at the center of the screen
# root = turtle.getcanvas().winfo_toplevel()
# root.geometry("+{}+{}".format(screen_width // 2 - 600, screen_height // 2 - 600))

# # Draw the spiral
# for i in range(turns):
#     turtle.circle(length, angle)
#     length *= phi

# # Hide the turtle
# turtle.hideturtle()

# # Keep the window open until the user closes it
# turtle.exitonclick()

'''
  The display was still out of bounds, only at the top left, not the top center.
  Let's try again.

  Q: The screen is popping up at the top left corner now, not the center. Could you fix this for me?

  A: Certainly! It looks like there is a problem with the calculation of the screen width and height.
  Here is a modified version of the program that correctly calculates the screen width and height:

    **code is given**

  This program correctly calculates the screen width and height using the turtle.window_width()
  and turtle.window_height() functions, which return the width and height of the screen in pixels.
  The window is then positioned at the center of the screen using the root.geometry() function.

  I hope this helps! Let me know if you have any questions.
'''

# import turtle
# import tkinter as tk

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

# # Get the screen width and height
# screen_width = turtle.window_width()
# screen_height = turtle.window_height()

# # Position the window at the center of the screen
# root = turtle.getcanvas().winfo_toplevel()
# root.geometry("+{}+{}".format(screen_width // 2 - 600, screen_height // 2 - 600))

# # Draw the spiral
# for i in range(turns):
#     turtle.circle(length, angle)
#     length *= phi

# # Hide the turtle
# turtle.hideturtle()

# # Keep the window open until the user closes it
# turtle.exitonclick()

'''
  Still not quite there. I want a natural viewing window, not smack dab at the corner of the screen.

  Q: Could you adjust the screen down a tad?

  A: Certainly! Here is a modified version of the program that positions the window slightly lower
  on the screen:

    **code is given**

  This program positions the window 100 pixels lower on the screen by modifying the value passed
  to the root.geometry() function.

  I hope this helps! Let me know if you have any questions.
'''

# import turtle
# import tkinter as tk

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

# # Get the screen width and height
# screen_width = turtle.window_width()
# screen_height = turtle.window_height()

# # Position the window slightly lower on the screen
# root = turtle.getcanvas().winfo_toplevel()
# root.geometry("+{}+{}".format(screen_width // 2 - 600, screen_height // 2 - 600 - 100))

# # Draw the spiral
# for i in range(turns):
#     turtle.circle(length, angle)
#     length *= phi

# # Hide the turtle
# turtle.hideturtle()

# # Keep the window open until the user closes it
# turtle.exitonclick()

'''
  Oops! ChatGPT made a mistake! Subtracting 100 puts the screen further up, not down.
  Let's correct it.

  Q: It appears that subtracting 100 pushed the screen further up, not down. Could you fix this?

  A: Certainly! It looks like there was a mistake in the calculation of the y-coordinate for the
  window position. Here is a modified version of the program that correctly positions the window
  lower on the screen:

    **code is given**

  Certainly! It looks like there was a mistake in the calculation of the y-coordinate for the
  window position. Here is a modified version of the program that correctly positions the window
  lower on the screen:
'''

# import turtle
# import tkinter as tk

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

# # Get the screen width and height
# screen_width = turtle.window_width()
# screen_height = turtle.window_height()

# # Position the window at the center of the screen
# root = turtle.getcanvas().winfo_toplevel()
# root.geometry("+{}+{}".format(screen_width // 2 - 600, screen_height // 2 - 600))

# # Draw the spiral
# for i in range(turns):
#     turtle.circle(length, angle)
#     length *= phi

# # Hide the turtle
# turtle.hideturtle()

# # Keep the window open until the user closes it
# turtle.exitonclick()

'''
  Almost there... It seems ChatGPT has issues tweaking specific values for small adjustments.
  Let's just try to make it fullscreen.

  Q: Could you make it full screen?

  A: Certainly! Here is a modified version of the program that opens the window in full screen mode:

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

# Get the screen width and height
screen_width = turtle.window_width()
screen_height = turtle.window_height()

# Open the window in full screen mode
root = turtle.getcanvas().winfo_toplevel()
root.attributes("-fullscreen", True)

# Draw the spiral
for i in range(turns):
    turtle.circle(length, angle)
    length *= phi

# Hide the turtle
turtle.hideturtle()

# Keep the window open until the user closes it
turtle.exitonclick()

'''
  We got the dimensions working (kind of), but the drawing isn't quite what I was looking for.
'''