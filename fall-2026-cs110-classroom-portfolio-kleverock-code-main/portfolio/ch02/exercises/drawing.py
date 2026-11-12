import turtle
my_turtle_obj = turtle.Turtle()
input("Pick a number for the number of sides and length of each side. Press Enter to continue")
side_num = input("How many sides do you want for your shape?")
length = int(input("What is the length of your sides:"))
angle = 360 / int(side_num)
window = turtle.Screen()
my_turtle_obj.shape("turtle")
my_turtle_obj.color("magenta")
my_turtle_obj.pensize(4)
for i in range(int(side_num)):
     my_turtle_obj.forward(length)
     my_turtle_obj.right(angle)

     
    




window.exitonclick()

  

