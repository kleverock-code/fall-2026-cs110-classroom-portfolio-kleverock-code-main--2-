import sys
userinput = " "
while userinput != "":
    userinput = input("Write a message")
    with open("demofile.txt", "w") as f:
        f.write("Added your input to the file")
    with open("demofile.txt") as f:
        print(f.read())
    if userinput == "":
        print("Thats okay, goodbye")
        sys.exit()