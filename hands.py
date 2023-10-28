import turtle

# Create a Turtle screen
window = turtle.Screen()
window.bgcolor("white")

# Create a Turtle object for drawing the middle finger
middle_finger = turtle.Turtle()
middle_finger.shape("turtle")
middle_finger.color("brown")

# Position the middle finger
middle_finger.penup()
middle_finger.goto(0, -50)  # Move the finger down from the center of the palm
middle_finger.setheading(90)  # Point the finger upwards
middle_finger.pendown()

# Draw the middle finger
middle_finger.begin_fill()
middle_finger.forward(80)  # Length of the middle finger
middle_finger.left(90)
middle_finger.forward(20)  # Width of the middle finger
middle_finger.left(90)
middle_finger.forward(80)
middle_finger.left(90)
middle_finger.forward(20)
middle_finger.end_fill()

# Close the Turtle graphics window on click
window.exitonclick()
