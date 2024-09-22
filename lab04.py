import turtle
import random

def draw_square(t , length):
    for _ in range(4):
        t.forward(length)
        t.left(90)

def draw_circle(t , radius):
    t.circle(radius)

def draw_polygon(t, sides, length):
    angle = 360 / sides
    for _ in range(sides):
        t.forward(length)
        t.left(angle)

def draw_pumpkin(t, x, y, radius):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor("orange")
    t.begin_fill()
    t.circle(radius)
    t.end_fill()
    t.fillcolor("green")
    t.begin_fill()
    t.left(90)
    t.forward(radius // 5)
    t.left(90)
    t.forward(radius // 5)
    t.left(90)
    t.forward(radius // 2)
    t.left(90)
    t.forward(radius // 2)
    t.end_fill()

def draw_eye(t, x, y, size):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.fillcolor("yellow")
    t.begin_fill()
    draw_polygon(t, 3, size)
    t.end_fill()

def draw_mouth(t, x, y, width):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.fillcolor("yellow")
    t.begin_fill()
    for _ in range(5):
        t.forward(width // 5)
        t.right(90)
        t.forward(width // 5)
        t.left(115)
    t.end_fill()

def draw_star(t, x , y, size):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor("white")
    t.begin_fill()
    for _ in range(5):
        t.forward(size)
        t.right(144)
    t.end_fill()

def draw_sky(t, num_stars):
    for _ in range(num_stars):

        x = random.randint(-600, 600)
        y= random.randint(90, 250)
        size = random.randint(10, 30)
        draw_star(t, x, y, size)


# Create a turtle object
t = turtle.Turtle()

# Hide the turtle and set speed
t.speed(0)  # 1 is slow, 10 is fast, 0 is instant
t.hideturtle()

# Create a window to draw in
# Create a new turtle screen and set its background color
screen = turtle.Screen()
screen.bgcolor("darkblue")
# Set the width and height of the screen
screen.setup(width=720, height=480)
# Clear the screen
t.clear()

screen = turtle.Screen()
screen.bgcolor("black")

"""PUT YOUR DRAW CALLS TO FUNCTIONS HERE"""
draw_pumpkin(t, 0, 0, -100)
draw_eye(t, -40, -90, 30)
draw_eye(t, 40, -90, 30)
draw_mouth(t, -50, -140, 100)

draw_sky(t, 50)
# Close the turtle graphics window when clicked
turtle.exitonclick()