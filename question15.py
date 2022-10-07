# Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn
def calculate(n):

    term2 = n*10+n
    term3 = n*100+n*10+n

    return n + term2 + term3

num = int(input("enter the integer : "))
print("Result : ",calculate(num))