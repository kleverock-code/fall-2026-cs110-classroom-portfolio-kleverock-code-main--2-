# Part A

weeks = 16
classes = 5
tuition = 6000

cost_per_week = (tuition / classes) / weeks
print("Cost per week:", cost_per_week)

student_age = 18
print(student_age, type(student_age))

classes_per_week = 3
print(classes_per_week, type(classes_per_week))  
print("Your total cost per week is:", cost_per_week)

cost_per_class = cost_per_week / classes_per_week 
print(cost_per_class, type(cost_per_class))

print("The cost per class is:", cost_per_class)
#Part B
import random
salad = ["Caesar", "Greek", "Cobb", "Garden", "Pasta"]
print(salad,type (salad))
random_salad = random.choice(salad)
print(random_salad,type (random_salad))
print("The random salad is:", random_salad)
#Part C
import random
def main():
    salad = ["Caesar", "Greek", "Cobb", "Garden", "Pasta"]
    print(salad, type(salad))
    random_salad = random.choice(salad)
    print(random_salad, type(random_salad))
    print("The random salad is:", random_salad)
main()



