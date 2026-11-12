a = 3
b = 5
def my_mult(a,b):
    a = 3
    b = 5
    result = 0


    for i in range(abs(b)):
        result = result + a

    if b >= 0:
        return result
    else:
        return -result

def power(base, exp):
    result = 1
    for i in range(exp):
     result = my_mult(result, base)
    return result
def square(num):
    power(num,2)

final_answer = square(3)

print("3 to the power 5 is", final_answer)




