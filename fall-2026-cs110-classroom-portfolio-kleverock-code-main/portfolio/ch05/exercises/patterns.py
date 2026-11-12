#Input function will take the input as the string value
star_pyramid = int(input("Enter the number of rows for your star pyramid:"))
 # int([x]) => integer
 #int(x, base=10) => integer
#That integer import will be stored in the variable
# #of rows will be stored in the variable
for i in range(star_pyramid):
    for column in range(star_pyramid-i-1):
        print("  ", end="")
    for column in range(i+1):
        print(" *",end="")
    print()
    
print(                                                                  )
for i in range(star_pyramid):
    # Step 1: Spaces now increase as i increases
    for column in range(i):
        print("  ", end="")
    # Step 2: Stars now decrease as i increases
    for column in range(star_pyramid - i):
        print(" *", end="")
    print()

 
    
    