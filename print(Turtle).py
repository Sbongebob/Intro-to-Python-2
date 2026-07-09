import turtle

# Screen Setup
screen = turtle.Screen()
screen.title("Snoopy")
screen.bgcolor("skyblue")

t = turtle.Turtle()
t.speed(0)
t.pensize(2)

# Helper Function
def move(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

# Head
move(0, 50)
t.color("black", "white")
t.begin_fill()
t.circle(60)
t.end_fill()

# Left Ear
move(-40, 120)
t.color("black", "black")
t.begin_fill()
t.setheading(210)
t.circle(40, 180)
t.right(90)
t.forward(40)
t.end_fill()

# Right Ear
move(40, 120)
t.begin_fill()
t.setheading(-30)
t.circle(-40, 180)
t.left(90)
t.forward(40)
t.end_fill()

# Nose
move(0, 55)
t.color("black", "black")
t.begin_fill()
t.circle(8)
t.end_fill()

# Eyes
move(-15, 95)
t.dot(8, "black")

move(15, 95)
t.dot(8, "black")

# Smile
move(-15, 45)
t.setheading(-60)
t.circle(25, 120)

# Body
move(0, -80)
t.color("black", "white")
t.begin_fill()
t.setheading(0)

for _ in range(2):
    t.circle(45, 90)
    t.circle(90, 90)

t.end_fill()

# Arms
move(-35, -30)
t.setheading(220)
t.forward(45)

move(35, -30)
t.setheading(-40)
t.forward(45)

# Legs
move(-20, -165)
t.setheading(-90)
t.forward(45)

move(20, -165)
t.forward(45)

# Feet
move(-20, -210)
t.begin_fill()
t.circle(10)
t.end_fill()

move(20, -210)
t.begin_fill()
t.circle(10)
t.end_fill()

# Tail
move(45, -120)
t.setheading(330)
t.forward(30)

# Collar
move(-35, -15)
t.color("red")
t.pensize(6)
t.setheading(0)
t.forward(70)

# Finish
t.hideturtle()

screen.mainloop()