#Ask the user to input the length and width of a rectangle and then calculate the area and perimeter

import math_module
'''def area(length, width):
    return length*width
def parameter(length, width):
    return 2*(length+width) '''

length=float(input("Enter the length of the rectangle: "))
width=float(input("Enter the width of the rectangle: "))

print("----Calculating Area------")
print(f"The area of the rectangle is: {math_module.area(length,width)}")
print()
print("----Calculating Perimeter------")
print(f"The Perimeter of the rectangle is: {math_module.parameter(length,width)}")

'''Enter the length of the rectangle: 10
Enter the length of the rectangle: 10
Enter the width of the rectangle: 5
----Calculating Area------
The area of the rectangle is: 50.0

----Calculating Perimeter------
The Perimeter of the rectangle is: 30.0
'''