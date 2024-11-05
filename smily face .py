import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle for the face
face = turtle.Turtle()
face.speed(3)

# Draw the face (circle)
face.penup()
face.goto(0, -100)
face.pendown()
face.color("yellow")
face.begin_fill()
face.circle(100)
face.end_fill()

# Draw the left eye
face.penup()
face.goto(-35, 35)
face.setheading(0)
face.color("black")
face.pendown()
face.begin_fill()
face.circle(10)
face.end_fill()

# Draw the right eye
face.penup()
face.goto(35, 35)
face.setheading(0)
face.pendown()
face.begin_fill()
face.circle(10)
face.end_fill()

# Draw the smile
face.penup()
face.goto(-40, 0)
face.setheading(-60)
face.width(5)
face.pendown()
face.circle(50, 120)  # Draw a semi-circle for the smile

# Hide the turtle and finish
face.hideturtle()
turtle.done()

