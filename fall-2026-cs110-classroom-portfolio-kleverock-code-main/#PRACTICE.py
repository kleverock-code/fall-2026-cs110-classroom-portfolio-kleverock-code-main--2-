#PRACTICE
"""Making a journal and writing on the page Im going to pass this class

FOUNDATION OF FILE HANDLING """
with open("my_journal_txt", "w") as file:
    file.write("I am going to pass this class.")
    
#CREATING A DICTIONARY ABOUT A STUDENT
student = {
    "name": "Alex",
    "major": "Computer Science",
    "gpa": "3.8" 
}
#KEEPING INFO ABOUT STUDENT IN DICTIONARY

print(student["name"])
print(student["major"])
print(student["gpa"])

#-----------------------------------------------#
grades = [19.20,21,25]
todo_list = ["do homework", "sleep", "eat"]

print(todo_list)
#-----------LIST OF DICTIONARIES---------------#
classroom = [
    {"name":"Alex", "major":"CS"},
    {"name":"Nathan", "major": "History"},
    {"name": "Marissa", "major": "Music"}
]
for student in classroom:
    print(student["name"])