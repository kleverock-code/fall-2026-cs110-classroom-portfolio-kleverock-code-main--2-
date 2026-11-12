import turtle
#-----------------------------#
screen = turtle.Screen()
screen.setup(width=500, height=500)
turtle.colormode(255)
screen.title("Little Butterfly")

BLACK = (0,0,0)
BLUE = (111,165,201)
DARKGREEN = (18, 150, 20)
PINK = (252, 104, 247)
PURPLE = (98, 30, 186)
#------------------------------#
leaf = turtle.Turtle()
butterfly = turtle.Turtle()
wings = turtle.Turtle()
antenna = turtle.Turtle()

wings.speed("fast")
butterfly.speed(0)
wings.speed(0)
leaf.speed(0)

radius = 60
distance = 95
start_x = -50  
start_y = 50   
screen.bgcolor(BLUE)
#-----ANTENNA-------#
def draw_antenna():
    """
    DRAWS BUTTERFLY'S ANTENNAS ONTOP OF HEAD
    """
    for i in range(2):
        antenna.hideturtle()
        antenna.color(BLACK)
        antenna.penup()
        antenna.goto(-5,130)
        antenna.backward(7)
        antenna.setheading(120)
        antenna.pendown()
        antenna.pensize(3)
        antenna.forward(40)
        antenna.dot()
    
#------LEAF--------#
def leaf_turtle():
    """ MAKES LEAF BELOW BUTTERFLY """
    leaf.penup()
    leaf.color(DARKGREEN)
    leaf.goto(100,-200)
    leaf.shape("circle")
    leaf.shapesize(8,24,10)
    leaf.stamp()
    leaf.color(DARKGREEN)
    leaf.goto(-200,-200)
    leaf.pensize(5)
    leaf.pendown()
    leaf.forward(200)
#------WINGS-------#
def draw_wings():
    """ DRAWS WINGS CONNECTED TO BUTTERFLY BODY"""
    for row in range(2):
        current_y = start_y - (row * distance)
    
        for column in range(2):
            current_x = start_x + (column * distance)
            wings.penup()
            wings.goto(current_x, current_y)
            wings.pendown()
            wings.pensize(10)
            wings.color(PURPLE, PINK)
            wings.begin_fill()
            wings.circle(radius)
            wings.end_fill()
#------BODY------#
def calculate_size(base):
    """CALCULCATES THE SIZE FOR THE BASE USED FOR BUTTERFLY BODY AND HEAD
    ARGS: BASE
    RETURN: MULTIPLIED RADIUS VALUE (BASE * 2)"""
    return base * 2
def head(butterfly, size):
    """DRAWS THE HEAD OF THE BUTTERFLY USING SPECIFIC RADIUS PARAMETER PREVIOUSLY FOUND
    ARGS: BUTTERFLY (THE TARGET), RADIUS SIZE OF THE HEAD """
    butterfly.penup()
    butterfly.circle(size)
    butterfly.color("black")
    butterfly.goto(-5,125)
    butterfly.shape("circle")
    butterfly.circle(19)
    butterfly.stamp()
def body(butterfly, size):
    """DRAWS THE BODY OF THE BUTTERFLY USING ELONGATED CIRCLE FOR BUTTERFLY FRAME
    ARGS: BUTTERFLY (TARGET), RADIUS SIZE OF BODY """
    butterfly.setheading(180)
    butterfly.color("black")
    butterfly.goto(-5,50)
    butterfly.shape("circle")
    butterfly.shapesize(7.25, 1.25) 
    butterfly.stamp()
def main(): 
    leaf_turtle()
    draw_wings()
    head_radius = calculate_size(3)
    head(butterfly, head_radius)
    body(butterfly, 3)
    
    draw_antenna()
    

main()
turtle.done()