#instructions
"""
Write a program that determines the letter grade for a course according to the following scale:

A >= 90

B >= 80

C >= 70

D >= 60

F < 60
"""

#Core requirements
"""
1. Ask the user for their grade percentage, then write a series of if-elif-else statements to print out the appropriate letter grade.
    (At this point, you'll have a separate print statement for each grade letter in the appropriate block.)

2. Assume that you must have at least a 70 to pass the class. After determining the letter grade and printing it out.
    Add a separate if statement to determine if the user passed the course, and if so display a message to congratulate them.
    If not, display a different message to encourage them for next time.

3. Change your code from the first part, so that instead of printing the letter grade in the body of each if, elif, or else block,
    instead create a new variable called letter and then in each block, set this variable to the appropriate value.
    Finally, after the whole series of if-elif-else statements, have a single print statement that prints the letter grade once.
"""

#stretch challanges
"""
1. Add to your code the ability to include a "+" or "-" next to the letter grade, such as B+ or A-.
    >For each grade, you'll know it is a "+" if the last digit is >= 7. You'll know it is a minus if the last digit is < 3 and otherwise it has no sign.
    >After your logic to determine the grade letter, add another section to determine the sign. 
    >Save this sign into a variable. 
    >Then, display both the grade letter and the sign in one print statement.
    >Hint: To get the last digit, you could divide the number by 10, and get the remainder. 
        You might refer back to the Week 02 preparation material to see the operators and find the one that does division and gives you the remainder.
    >At this point, don't worry about the exceptional cases of A+, F+, or F-.

2. Recognize that there is no A+ grade, only A and A-. Add some additional logic to your program to detect this case and handle it correctly.

3. Similarly, recognize that there is no F+ or F- grades, only F. Add additional logic to your program to detect these cases and handle them correctly.
"""

#ask user for grade percentage
grade = float(input("What is your grade percentage? "))
#grade = 30
grade_letter = ""
grade_sign = ""
remainder = grade % 10

#determine grade later based on grade provided by user
if grade >= 90 :
    grade_letter = "A"
elif grade <= 89 and grade >= 80 :
    grade_letter = "B"
elif grade <= 79 and grade >= 70 :
    grade_letter = "C"
elif grade <= 69 and grade >= 60 :
    grade_letter = "D"
else :
    grade_letter = "F"

#determine remainder to add + or - to grade letter
if grade_letter != "F" and grade <= 93 and remainder >= 7 or grade >= 100:
    grade_sign = "+"
elif grade_letter != "F" and remainder <= 3 :
    grade_sign = "-"

#print grade letter and deterime if user passed the course
print(f"You recevied an {grade_letter}{grade_sign}.")

if grade >= 70:
    print(f"You have passed the course by having more than 70%.")
else:
    print(f"Your grade was {grade:.2f}% and you need atleast 70% to pass this course. Please try agian next time.")