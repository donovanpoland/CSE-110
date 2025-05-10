
# do this to make commments
# use_snake_case_for_variables this is a python convention for vaiables

#instructions
"""An iconic line from the James Bond movies is that he would introduce himself as "Bond, James Bond."
 For this assignment you will write a program that asks for your name and repeats it back in this way."""

first_name =input("Please enter your first name?\n")
last_name =input("Please enter your last name?\n")
#make name statement to the user re-useable
statement = "Your name is "
#smaller vairable useage per line
full_name = first_name + " " + last_name
#using capitalize function on a variable instead of using it in the string to refactor the users input to captitalize the input
cap_first_name = first_name.capitalize()
cap_last_name = last_name.capitalize()
cap_full_name = cap_first_name + " " + cap_last_name

# #one way to display (longer) no formating
print("Your name is " + last_name + ", " + first_name + " " + last_name + ".")

#alt way to display full name (extra variable but shorter lines aka more readable)
print("Your name is " + last_name + ", " + full_name + ".")

#capitallize user input (re-used code should be in a variable)
print(statement + last_name.capitalize() + ", " + first_name.capitalize() + " " + last_name.capitalize() + ".")

#full name capitalized to shorten code line readability
print(statement + last_name.capitalize() + ", " + full_name.capitalize() + ".")

#single use of capitalize where the original variable is stored so you dont have to do it every time the name is used.
print(statement + cap_last_name + ", " + cap_full_name + ".")

"""examples above are another way of useing output (note "output" is just a variable and can be anything)"""

output = "output: Hello, " + first_name + " " + last_name
output1 = "output1: " + statement + cap_full_name
output2 = "output2: Your name is {} {}".format(first_name, last_name)
print(output)
print(output1)
print(output2)

# use {} as a place holder for a variable inside your string (this is a fancy way of putting spaces between your variables without doing "+ ' ' +" every time
# just do "{}(space right here){}" aka " {} {} ")
output3 =  "{} {} {}".format(statement, cap_first_name, cap_last_name)#the space at the end of variable "statement" results in double spacing from .format
print("output3: " + output3)

# only useable in py3.0 + (f is the short form of .format this will shorten the statement even more by placing the variable directly inside {} instead of using a placeholder)
output4 = f"output4: Hello, {first_name} {last_name}"
print(output4)
output5 = f"output5: Your name is {cap_first_name} {cap_last_name}"
print(output5)
output6 = f"output6: {statement}{cap_first_name} {cap_last_name}"
print(output6)
output7 = f"output7: {statement}{cap_full_name}"
print(output7)

""" Examples of other string functions including .title(), .upper(), .lower(), .count("A"), .lower().count("a"), .upper().count("A") """

print("using .title()")
title1 = f"{statement}{last_name.title()} {first_name.title()} {last_name.title()}"#carefull were you place your spaces or you will get doubles
print(title1)

title2 = f"{statement}{last_name}, {first_name} {last_name}"
print(title2.title())

