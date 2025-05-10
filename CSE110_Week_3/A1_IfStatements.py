#instructions
"""
Activity Instructions
    Practice writing programs that compare strings and numbers.

Comparing Numbers
    Write a program that asks the user for two integers.

    Then, write three separate if/else statements as follows:

        >If the first number is greater than the second, print "The first number is greater". Otherwise, print "The first number is not greater".
        >If the two numbers are equal print "The numbers are equal". Otherwise, print "The numbers are not equal".
        >If the second number is greater than the first, print "The second number is greater". Otherwise, print "The second number is not greater".

Comparing Strings
    Have the program ask the user for their favorite animal. Then write an if statement as follows:

        >Check to see if the user's favorite animal is the same as your favorite animal (meaning you, the programmer). 
            If it is, print "That's my favorite animal too!" If it's not, print "That one is not my favorite."
            Verify that it works regardless of the capitalization.
"""

#testing
""" 
1. Test the first part of your program with pairs of numbers where the first is greater and also where the second is greater. Verify that all three values that are printed are correct.
2. Test it with two numbers that are equal. Verify that all three values that are printed are correct.
3. Test the second part of your program with an animal that is different. Verify that the correct message is shown.
4. Test it with an animal that is the same. Verify that the correct message is shown.
5. Test it with an animal that is the same, but using different capitalization. Verify that it still matches, even with different capitalization.
"""

# #test first number is greater
# first_number = 20
# second_number = 16

# #test second number is greater
# first_number = 16
# second_number = 20

# #testing equal numbers
# first_number = 16
# second_number = 16

#ask user for number / int converstion of input
first_number = int(input("What is the first number? "))
second_number = int(input("What is the second number? "))

#if 1
if first_number > second_number:
    print("The first number is greater")
else:
    print("The first number is not greater")
    
#if 2
if first_number == second_number:
    print("The numbers are equal")
else:
    print("The numbers are not equal")

#if 3
if second_number > first_number:
    print("The second number is greater")
else:
    print("The second number is not greater")

#compare strings
my_fav_animal = "fox"
user_animal = input("\nWhat is your favorite animal? ")
if my_fav_animal == user_animal.lower():
    print("That's my favorite animal too!")
else:
    print("That one is not my favorite.")