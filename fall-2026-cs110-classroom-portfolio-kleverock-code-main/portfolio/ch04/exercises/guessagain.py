import random
random_number = random.randint(1,1000)
guesses = 0
input("I am thinking of a number between one and a thousand. You will have as many attempts as you need to guess the correct number.")
for i in range(random_number):
    guess = int(input("Please type your guess."))
    guesses += 1

    if guess < random_number:
        print("Too low! Try again?")
    elif guess > random_number:
        print("Too high! Try again?")
    else:
        print("Wow! You guessed it correctly! It took you", {guesses}, "guesses!")
        break
    
        
print("The random number was", random_number)
        