import turtle

# Create the screen
screen = turtle.Screen()
screen.title("Stick Person")

# Create the turtle
t = turtle.Turtle()
t.shape("turtle")
t.speed(5)
t.pensize(3)
t.pencolor("black")

# Head
t.penup()
t.goto(0, 100)
t.pendown()
t.circle(30)

# Body
t.right(90)
t.forward(100)

# Left arm
t.backward(70)
t.left(45)
t.forward(50)

# Back to body
t.backward(50)
t.right(90)

# Right arm
t.forward(50)
t.backward(50)

# Back to body
t.left(45)
t.forward(70)

# Left leg
t.left(45)
t.forward(60)

# Back to bottom of body
t.backward(60)
t.right(90)

# Right leg
t.forward(60)

# Keep the window open
screen.mainloop()
