# a function that checks whether a number is in a given range 
def checkRange(num,high,low):
    if(low <= num and num <= high):
        return True
    else:
        return False

high = int(input("enter the highest value "))
low = int(input("enter the lowest value "))
num = int(input("enter the number to be checked "))

if(checkRange(num,high,low) == True):
    print("{}  is within the range".format(num))
else:
    print("{}  is not within the range".format(num))
