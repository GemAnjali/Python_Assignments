from audioop import add


# Write a Python program to display your details like name, age, address in three different lines.

def details(name, age, address):
    print("Name : {}\nAge : {}\nAddress : {}".format(name,age,address))

name , age = "Sally",20
address = "Bangalore, Karnataka"
details(name,age,address)