# Write a Python function that checks whether a passed string is palindrome or not
def palindrome(text):
    revstr = ""
    revstr = text[::-1]
    return revstr

text = input("enter the string : ")  
result = palindrome(text)

if result == text:
    print("{} is Palindrome".format(text))
else:
    print("{} is not Palindrome".format(text))
