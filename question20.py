# a Python program to solve (x + y) * (x + y).
def solveEquation(x,y):
    result = x*x + y*y + 2*x*y
    return result

num1 = int(input("enter the value of x : "))
num2 = int(input("enter the value of y : "))

result = solveEquation(num1,num2)
print("({} + {}) * ({} + {}) = {}".format(num1,num2,num1,num2,result))