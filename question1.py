# Python program that accepts a hyphen-separated sequence of words as input 
# and prints the words in a hyphen-separated sequence after sorting them
# alphabetically.

def alphabeticalOrder():

    str = input("Enter hyphen separated sequence of words : ")
    listOfWords = str.split("-")

    #sorting the list
    listOfWords.sort()
    print("-".join(listOfWords))

alphabeticalOrder()


