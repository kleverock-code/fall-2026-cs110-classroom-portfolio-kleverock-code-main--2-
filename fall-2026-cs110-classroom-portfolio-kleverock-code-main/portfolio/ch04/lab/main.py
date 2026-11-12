import turtle
import random
import math
def main():
    screen = turtle.Screen()
    screen.bgcolor("violet")
    
    # 
    screen_width = 600
    screen_height = 500
    screen.setup(screen_width, screen_height)
    
    dartboard_radius = 100
    dartboard = turtle.Turtle()
    dartboard.speed(0)
    dartboard.hideturtle()  # Hides the drawing icon so it renders cleanly
    dartboard.pensize(5)
    
    # 
    dartboard.up()
    dartboard.goto(0, -100)
    dartboard.down()
    dartboard.color("black", "gold")
    dartboard.begin_fill()
    dartboard.circle(100)
    dartboard.end_fill()
    
    # 
    dartboard.up()
    dartboard.goto(0, -75)
    dartboard.down()
    dartboard.color("black", "orange")
    dartboard.begin_fill()
    dartboard.circle(75)
    dartboard.end_fill()
    
    # 
    dartboard.up()
    dartboard.goto(0, -50)
    dartboard.down()
    dartboard.color("black", "yellow")
    dartboard.begin_fill()
    dartboard.circle(50)
    dartboard.end_fill()
    
    # 
    dartboard.up()
    dartboard.goto(0, -25)
    dartboard.down()
    dartboard.color("black", "orange")
    dartboard.begin_fill()
    dartboard.circle(25)
    dartboard.end_fill()

    # PART B: USER INPUT
   #BETTING
    user_guess = screen.textinput("Player Prediction","Which player do you think will get the most points? Enter Red or Blue.")
    if user_guess is not None:
        user_guess = user_guess.lower().strip()
    while user_guess not in ["red", "blue"] and user_guess is not None:
        user_guess = screen.textinput("Sorry that's an invalid input.", "Please enter Red or Blue")
        if user_guess is not None:
            user_guess = user_guess.lower().strip()
        
        
    
        
    
        
    # DART THROWING
    total_darts = 10  # 10 darts per player
    dart = turtle.Turtle()
    dart.speed(0)
    dart.hideturtle()
    
    player1_score = 0
    player2_score = 0
        
    # 
    for i in range(total_darts):
        dart_x = random.uniform(-screen_width / 2, screen_width / 2)
        dart_y = random.uniform(-screen_height / 2, screen_height / 2)
        
        distance_from_center = math.hypot(dart_x, dart_y)
        
        if distance_from_center <= dartboard_radius:
            dart.color("white")
            player1_score += 1
        else:
            dart.color("blue")
            
        dart.up()
        dart.goto(dart_x, dart_y)
        dart.dot(10)

    # 
    for i in range(total_darts):
        dart_x = random.uniform(-screen_width / 2, screen_width / 2)
        dart_y = random.uniform(-screen_height / 2, screen_height / 2)
        
        distance_from_center = math.hypot(dart_x, dart_y)
        
        if distance_from_center <= dartboard_radius:
            dart.color("green")
            player2_score += 1
        else:
            dart.color("red")
            
        dart.up()
        dart.goto(dart_x, dart_y)
        dart.dot(10)
        
    # 
    turtle.penup()
    turtle.goto(0, -150)
    turtle.write(f"Player 1 Score: {player1_score}", align="center", font=("Arial", 16, "normal"))
    
    turtle.goto(0, -175)
    turtle.write(f"Player 2 Score: {player2_score}", align="center", font=("Arial", 16, "normal"))
    
    turtle.goto(0, -210)
    if player1_score == player2_score:
        print("Tie!")
        turtle.write("Tie! Neither Player won", align="center", font=("Arial", 18, "bold"))
    elif player1_score > player2_score:
        print("Player 1 Wins!")
        turtle.write("Player 1 Wins!", align="center", font=("Arial", 18, "bold"))
        turtle.goto(0,-230)
        if user_guess == "blue":
            turtle.write("Your prediction was correct!", align="center", font=("Arial", 18, "bold"))
        else:
            turtle.write("Your prediction was incorrect!", align="center", font=("Arial", 18, "bold"))
            
    else:
        print("Player 2 Wins!")
        turtle.write("Player 2 Wins!", align="center", font=("Arial", 18, "bold"))
        turtle.goto(0,-230)
        if user_guess == "red":
            turtle.write("Your prediction was correct!", align="center", font=("Arial", 18, "bold"))
        else:
            turtle.write("Your prediction was incorrect!", align="center", font=("Arial", 18, "bold"))
    screen.exitonclick()
main()




