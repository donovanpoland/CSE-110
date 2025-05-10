import math

quit = ""

# Can calculate if a square without a function or by using the rectangle fuction
# def compute_area_square (length):
#     area = float(length) * float(length)
#     return area

def compute_area_rectangle(length, width):
    area = float(length) * float(width)
    return area

def compute_area_circle(radius):
    pi = math.pi
    area = pi * (radius ** 2)
    return area

while quit.lower() != "quit":
    # Reset are to 0 after each loop
    area = 0
    # Ask for shape
    shape = input("\nWhat kind of shape do you have? ")

    shape = shape.lower()

    if shape == "square":
        length = float(input("What is the length of a side of the square? "))
        width = length
        area = compute_area_rectangle(length, width)
        print(f"The area of the square is: {area}")

    elif shape == "rectangle":
        length = float(input("What is the length of rectangle? "))
        width = float(input("What is the width of the retangle? "))
        area = compute_area_rectangle(length, width)
        print(f"The area of the rectangle is: {area}")

    elif shape == "circle":
        radius = float(input("What is the radius of the circle? "))
        area = compute_area_circle(radius)
        print(f"The area of the circle is: {area:.2f}")

    elif shape == "quit":
        # End loop
        print("Good bye.")
        quit = shape

    else:
        print("That is not a valid shape, try again.")
