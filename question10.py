# Python function to multiply all the numbers in a list

def multiply(numList):
    product = 1
    for i in range(len(numList)):
        product = product*numList[i]
    return product
    

numList = [1,2,3,-4]
print(multiply(numList))
