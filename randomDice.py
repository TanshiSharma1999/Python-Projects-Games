import turtle
import random

# Screen setup
sc = turtle.Screen()
sc.setup(400, 400)
sc.bgcolor("black")
sc.title("Dice Roll Simulation")

# Turtle setup
pen = turtle.Turtle()
pen.hideturtle()
pen.color("white")
pen.speed(0)

# Function to move turtle without drawing
def jump(x, y):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()

# Show title
jump(0, 100)
pen.write("Dice Roll Simulation", align="center", font=("Comic Sans MS", 24, "bold"))

# Show instruction
jump(0, 0)
pen.write("Press SPACE to Roll Dice", align="center", font=("Comic Sans MS", 18, "bold"))

# Function to roll dice
def roll_dice():
    pen.clear()
    number = random.randint(1, 6)
    pen.color("white")

    if number == 1:
        sc.bgcolor("blue")
        jump(0, 0)
        pen.dot(70)

    elif number == 2:
        sc.bgcolor("pink")
        jump(0, -70)
        pen.dot(70)
        jump(0, 70)
        pen.dot(70)

    elif number == 3:
        sc.bgcolor("orange")
        jump(0, -100)
        pen.dot(70)
        jump(0, 0)
        pen.dot(70)
        jump(0, 100)
        pen.dot(70)

    elif number == 4:
        sc.bgcolor("red")
        for x in (-70, 70):
            for y in (-70, 70):
                jump(x, y)
                pen.dot(70)

    elif number == 5:
        sc.bgcolor("purple")
        for x in (-70, 70):
            for y in (-70, 70):
                jump(x, y)
                pen.dot(70)
        jump(0, 0)
        pen.dot(70)

    elif number == 6:
        sc.bgcolor("green")
        for x in (-70, 70):
            for y in (-100, 0, 100):
                jump(x, y)
                pen.dot(70)

# Key binding
sc.listen()
sc.onkey(roll_dice, "space")

# Keep window open
turtle.mainloop()
