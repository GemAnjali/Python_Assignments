# Python function that takes a list and returns a new list with unique elements of the first list.

def uniqueList(numList):
    numset = set()
    return(list(set(numList)))

numList = [1,1,1,1,2,2,3,3,3,3,4,5]
print(uniqueList(numList))