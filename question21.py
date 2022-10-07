#a Python program to print out a set containing all the colors from color_list_1 which are not present in color_list_2.

def setDifference(cList1,cList2):
    return cList1 - cList2


color_list_1 = set(["white","Black","Red"])
color_list_2 = set(["Red","Green"])
print(setDifference(color_list_1,color_list_2))
