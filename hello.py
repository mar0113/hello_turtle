import turtle
import random

canvas = turtle.Canvas()

gang = []
for x in range(5):
    gang.append(turtle.Turtle())
    gang[x].shape("turtle")

# change all the turtles' color
for x in range(5):
    gang.append(turtle.Turtle())
    gang[x].color("green")

# move all the turtles to a random spot

for tommy in gang:
    tommy.penup()
    tommy.goto(random.randint(-200,200), random.randint(-200,200))

# EXTRA: make all of the turtles with an even index write a message

input("Press enter to quit")
