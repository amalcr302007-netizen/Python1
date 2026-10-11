
import math
import turtle
import time

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("I Love You ❤️")
screen.tracer(0)

t = turtle.Turtle()
t.hideturtle()
t.penup()
t.color("#ffb6c1")

for scale in range(11, 17):
    t.clear()

    for i in range(120):
        angle = i * (math.pi * 2) / 120

        x = 16 * (math.sin(angle) ** 3) * scale
        y = (
            13 * math.cos(angle)
            - 5 * math.cos(2 * angle)
            - 2 * math.cos(3 * angle)
            - math.cos(4 * angle)
        ) * scale

        t.goto(x, y)
        t.write(
            "I love you",
            align="center",
            font=("Arial", 8, "bold")
        )

    screen.update()
    time.sleep(0.3)

turtle.done()
