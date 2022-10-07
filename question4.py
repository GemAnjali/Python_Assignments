# a Python program to find the first duplicate element in a given array of integers

def duplicateElement(numList):
    numSet = set()
    noDuplicate = -1
    for i in range(len(numList)):
        if numList[i] in numSet:
            return numList[i]
        else:
            numSet.add(numList[i])
    return noDuplicate


duplicateList = [1,2,3,4,5,6,8.6,4,8]
print(duplicateElement(duplicateList))




