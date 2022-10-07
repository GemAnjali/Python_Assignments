# a Python function that accepts a string and calculate the number of upper case letters and lower case letters.
def findUpperAndLower(text):
    lowerCount = 0
    upperCount = 0

    for i in text:
        if i.islower():
            lowerCount = lowerCount+1
        if i.isupper():
            upperCount = upperCount+1
    print("Number of Upper case characters : ",upperCount)
    print("Number of lower case characters : ",lowerCount)


str = input("Enter the string : ")
findUpperAndLower(str)

