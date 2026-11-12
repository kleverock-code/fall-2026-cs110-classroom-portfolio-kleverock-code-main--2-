import random 
input("Pick any two numbers and I will generate a random number between them! Press Enter to continue")
low = input("Enter the lower number:")
high = input("Enter the higher number:")
num_numbers = input("How many random numbers would you like generated? ")
for i in range(int(num_numbers)):
    print("Your random number is", (random.randint(int(low), int(high))))
    