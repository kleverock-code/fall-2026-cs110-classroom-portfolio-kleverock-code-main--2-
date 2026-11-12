import turtle
import random
import math
def main():
    screen = turtle.Screen()
    screen.bgcolor("violet")
    screen.screensize()
    screen_size = screen.screensize()
    screen_width = screen_size[0]
    screen_height = screen_size[1]
    dartboard_radius = 100
    dartboard = turtle.Turtle()
    dartboard.speed(0)
    dartboard.pensize(5)
    dartboard.up()
    dartboard.goto(0,-100)
    dartboard.down()
    dartboard.color("black","gold")
    dartboard.begin_fill()
    dartboard.circle(100)
    dartboard.end_fill()
    dartboard.up()
    dartboard.goto(0,-75)
    dartboard.down()
    dartboard.color("black","orange")
    dartboard.begin_fill()
    dartboard.circle(75)
    dartboard.end_fill()
    dartboard.up()
    dartboard.goto(0,-50)
    dartboard.down()
    dartboard.color("black","yellow")
    dartboard.begin_fill()
    dartboard.circle(50)
    dartboard.end_fill()
    dartboard.up()
    dartboard.goto(0,-25)
    dartboard.down()
    dartboard.color("black","orange")
    dartboard.begin_fill()
    dartboard.circle(25)
    dartboard.end_fill()

#PART B

    dart=turtle.Turtle()
    dart.hideturtle()
    for i in range(10):
        dart_x = random.uniform(-screen_width / 2, screen_width / 2)
        dart_y = random.uniform(-screen_height / 2, screen_height / 2)
        distance_from_center = math.hypot(dart_x,dart_y)
        if distance_from_center <= dartboard_radius:
            dart.color("green")
        else:
            dart.color("red")
        dart.up()
        dart.goto(dart_x,dart_y)
        dart.dot()
        random_x = random.randint(-300,300)
        random_y = random.randint(-250,250)
        dart.goto(random_x, random_y)
    
    
    screen.exitonclick()
main()

