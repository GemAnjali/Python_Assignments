# Python program to accept a filename from the user and print the extension of that.
def findExtension(fileName):

    fileList  = fileName.split(".")
    return fileList


fileName = input("enter the file name : ")
result = findExtension(fileName)
print("extension of the file {} is {} ".format(fileName,result[-1]))