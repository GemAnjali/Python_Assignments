# a Python program to access a function inside a function
def rectangle(l,b):
    return(l*b)

def getDetails():
    length =int(input("enter length of the rectangle : "))
    width = int(input("enter width of the rectange : "))
    print("length of the rectangle = ",length)
    print("width of the rectangle = ",width)
    area = rectangle(length,width)
    print("area = ",area)

getDetails()




