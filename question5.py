# a Python program to get the number of occurrences of a specified element in an array
def countOccurence(num,numList):
    return numList.count(num)

numList = [10,12,44,11,90,54,44,12,77,12]
num = int(input("enter the number to count the frequency "))
result = countOccurence(num,numList)
print("Frequency is ",result)

