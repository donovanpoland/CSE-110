
"""Type casting or "casting" is a way of converting on data type into different data types """

print("Lets do some math")
print("Create your own math problem")
#this user input is stored as strings
str_x = input("Enter a number for x: ")
str_y = input("Enter a number for y: ")
#then converted into intigers or floating numbers
solution = (int(str_x) + int(str_y ))
solution2 = (float(str_x) + float(str_y ))
#then placed in a string again to display both solutions
print(str(solution) + " or " + str(solution2))

# data stored as floating mumber
float_pi = 3.14159
#stored as a floating number but converted to be stored as an intiger
int_pi = int(3.14159)
#stored as a string
str_pi = "3.14159"

# when data is printed it prints as its stored, if a float is added to a string the float must be converted to a str first
print("This flout is converted and printed as a string " + str(float_pi))
# this will take the 2 strings and piece them together
print("This pi is a string and printed as a string " + str_pi)
print()
print("Addition of 2 floats")
print(float_pi + float_pi)
print()
print("Addition of 2 ints")
print(int_pi + int_pi)
print()
print("Addition of int and float becomes a float")
print(int_pi + float_pi)
print()