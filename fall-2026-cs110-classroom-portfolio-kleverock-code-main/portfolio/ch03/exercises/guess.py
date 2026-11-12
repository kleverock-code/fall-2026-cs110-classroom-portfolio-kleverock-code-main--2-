import random
random_number = random.randint(1,10)
input("I am thinking of a number between one and ten. You will have three attempts to guess my number. Press Enter to continue.")
for i in range(3):
    guess = int(input("Please type your guess."))

    if guess < random_number:
        print("Too low! Try again?")
    elif guess > random_number:
        print("Too high! Try again?")
    else:
        print("Wow! You guessed it correctly!")
        break
    
        
print("The random number was", random_number)
        

        
