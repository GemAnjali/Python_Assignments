#Write a function that computes the volume of a sphere given its radius.

def calculateVolume(radius):
    pi = 3.14
    return (4/3)*pi*radius*radius*radius

radius = float(input("enter the radius of the sphere : "))
print("Volume of the sphere is ",calculateVolume(radius))