#  Python program that will return true if the two given integer values are equal or their sum or difference is 5.

def checkEqualSumDifference(num1,num2):
    if num1 == num2 or num1-num2 == 5 or num2-num1 == 5 or num1+num2 == 5:
        return True

int1 = int(input("enter first integer : "))
int2 = int(input("enter second integer : "))
if checkEqualSumDifference(int1,int2) == True:
    print("{} and {} satisfy the condition".format(int1,int2))
else:
    print("{} and {}  do not satisfy the condition".format(int1,int2))
    
    

