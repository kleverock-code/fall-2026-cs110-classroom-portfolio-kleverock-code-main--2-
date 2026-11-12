import turtle
import random
window = turtle.Screen()
    
my_turtle_obj = turtle.Turtle()
heads = 1
tails = 2

my_turtle_obj.goto(0,0) #changed this from turtle because used wrong variable
#This defines screen boundaries. Half of the width/height represents the distance to the edge from the center
max_x = window.window_width() / 2 
max_y = window.window_height() / 2

while True: 
    coinflip = random.randint(1, 2)
    if coinflip == heads:
             my_turtle_obj.left(90)
    else:
        my_turtle_obj.right(90)
    my_turtle_obj.forward(50)
#Must be indented to not be in the while loop
    current_x = my_turtle_obj.xcor()
    current_y = my_turtle_obj.ycor()

    if abs(current_x) > max_x or abs(current_y) > max_y:
        print("Out of bounds! Stopping.")
        break # This exits the loop

window.exitonclick()

    



