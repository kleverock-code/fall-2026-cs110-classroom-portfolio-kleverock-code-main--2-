import turtle  # 1. import modules
import random
# Part A
window = turtle.Screen()  # 2.  Create a screen
window.bgcolor("lightblue")

michelangelo = turtle.Turtle()  # 3.  Create two turtles
leonardo = turtle.Turtle()
michelangelo.color("orange")
leonardo.color("blue")
michelangelo.shape("turtle")
leonardo.shape("turtle")

michelangelo.up()  # 4. Pick up the pen so we don’t get lines
leonardo.up()
michelangelo.goto(-100, 20)
leonardo.goto(-100, -20)

## 5. Your PART A code goes here
michelangelo.forward(random.randrange(1,101))
leonardo.forward(random.randrange(1,101))
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)
for count in range(10):
    michelangelo.forward(random.randrange(1,11))
    leonardo.forward(random.randrange(1,11))
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)


# PART B - complete part B here
leonardo.pendown()
num_of_sides = 3
angle = 360 / num_of_sides
length = 100
for i in range(int(num_of_sides)):
    leonardo.forward(length)
    leonardo.right(angle)
leonardo.clear()

num_of_sides = 4
angle = 360 / num_of_sides
length = 100
for i in range(int(num_of_sides)):
    leonardo.forward(length)
    leonardo.right(angle)
leonardo.clear()

num_of_sides = 6
angle = 360 / num_of_sides
length = 100
for i in range(int(num_of_sides)):
    leonardo.forward(length)
    leonardo.right(angle)
leonardo.clear()

num_of_sides = 20
angle = 360 / num_of_sides
length = 20
for i in range(int(num_of_sides)):
    leonardo.forward(length)
    leonardo.right(angle)
leonardo.clear()

num_of_sides = 100
angle = 360 / num_of_sides
length = 2
for i in range(int(num_of_sides)):
    leonardo.forward(length)
    leonardo.right(angle)
leonardo.clear()

num_of_sides = 360
angle = 360 / num_of_sides
length = 2
for i in range(int(num_of_sides)):
    leonardo.forward(length)
    leonardo.right(angle)
leonardo.clear()

window.exitonclick()
    





    
    





