# Python program to check whether a specified value is contained in a group of values.
def checkOccurence(num,numList):
    if num in numList:
        return True

nList  = [1,5,8,3]
n = int(input("enter the number to be searched : "))
if(checkOccurence(n,nList) == True):
    print("True")
else:
    print("False")