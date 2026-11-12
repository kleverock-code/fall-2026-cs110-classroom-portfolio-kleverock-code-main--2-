import turtle
#PART A
#Calculates how many iterations it takes for one starting value to reach 1
def threenp1(n): 
    """Calculates how many itertations it takes for one starting value"""
    count = 0 
    while n > 1.0:
        if n % 2 == 0:
            n = int(n / 2) #add int b/c its an integer 
        else:
            n = int(3 * n + 1)
        count = count + 1
    return count #cant be nested in the loop
def threenp1range(upper_limit):
    objs_in_sequence = {}
    for i in range(2, upper_limit + 1):
         iterations = threenp1(i)
         objs_in_sequence[i] = iterations
        #if you just wrote (2, upper_limit, it would actually be upper_limit - 1 and would not include it)
    result = threenp1(i)
        #dont use return because it is disregards any code below it 
    return objs_in_sequence
#PART B
def graph_coordinates(threenplus1_iters_dict):
    #Draws the 3n+1 data using Turtle graphics.
    window = turtle.Screen()
    window.setworldcoordinates(0,0,10,10)
    my_turtle_obj = turtle.Turtle()
    max_so_far = 0
    my_turtle_obj2 = turtle.Turtle()
    my_turtle_obj2.up()
    my_turtle_obj2.hideturtle()
    for x, y in threenplus1_iters_dict.items():
        if y > max_so_far:
            max_so_far = y
            my_turtle_obj2.clear()
            my_turtle_obj2.goto(10, max_so_far + 5)
            my_turtle_obj2.write(f"Maximum so far:{max_so_far}")
            
        
        window.setworldcoordinates(0, 0, x + 10, max_so_far + 10)
        my_turtle_obj.goto(x, y)
def main():
    upper_limit = 10
    result_dict = threenp1range(upper_limit)
    graph_coordinates(result_dict)
    turtle.Screen().exitonclick()
main()


        
        
   

