import math

#instructions
"""
Write a program to compute the areas of three different shapes. Prompt for the necessary information, then compute and display the area, as follows:
Make sure that your program can appropriately handle decimal values as well as whole numbers.
1. Square—The area is the length of a side squared.
2. Rectangle—The area is the length multiplied by the width.
3. Circle—The area is Pi (you can use 3.14) multiplied by the radius squared.

"""

#stretch challange
"""
1. Instead of using 3.14 for your value of Pi, see if you can find and use the built-in value of Pi included in the python "math" module.
    Hint, you might try searching on the internet for something like, "python how to get the value of pi."
2. Prompt the user for a single length value, then compute and display the areas of a square with that length of side,
    a circle with that radius, and then the volumes of a cube with that side and a sphere with that radius, all from the same value from the user.
3. For each of the three areas in the core requirements, change the prompt for the user to ask for the value in centimeters. 
    Then, display the resulting area in both square centimeters and square meters. Keep in mind that a centimeter is 1/100 of a meter, and a square centimeter is 1/10,000 of a square meter.
"""

#area of a square/rectangle= L * W
#are of a circle = pi * radius squared (r^2)

pi = math.pi

measurement = input("Would you like your obejcts measured in metric or imperial? ")





#ask for input of a quare
length = input("What is the length of a side of the square? ")
area = float(length) * float(length)
print(f"The area of the square is: {str(area)}")

#ask for input of a rechtangle
length = input("What is the length of rectangle? ")
width = input("What is the width of the retangle? ")
area = float(length) * float(width)
print(f"The area of the rectangle is: {str(area)}")

#ask for radius of a circle
radius = float(input("What is the radius of the circle? "))
area = pi * (radius ** 2)
print(f"The area of the circle is: {area:.2f}")

input = float(input("What is the length of your shape? "))
radius = input
square = input ** 2
circle =  pi * (radius ** 2)
cube = input ** 3
sphere = 4/3 * pi * (radius ** 3)

print(f"The square would be {square} and the circle would be {circle} also a cube would be {cube} and a sphere would be {sphere}")