#Python function to check whether a string is pangram or not.
def pangrams(text):
    lowerCaseText = text.lower()
    spaceRemovedText = lowerCaseText.replace(" ","")
    textSet = set(spaceRemovedText)
    if len(textSet) == 26:
        return True


txt = input("enter the string : ")
result = pangrams(txt)
if result == True:
    print("{} is a Pangram".format(txt))
else:
    print("{} is not a Pangram".format(txt))

    




    
