# basic file entry and interaction
courses_file = open("courses.txt")
for each_line in courses_file:
    print(each_line)

# "with" will automaticly close the file when done using it.
# when you use "as" and then a variable name, such as courses you create a variable on the right instead of the left
# end with a semi colin to create an open statement
with open("courses.txt") as courses:
    # Continue like you would a loop or if statement, everying indented is what will happen when the file is open
    for line in courses:
        print(line.strip()) # .strip() removes the white spaceat the front and end of a string
# After you leave the indented stucture the file closes and the statement fisnishes 
print()

with open("courses.txt") as courses:
    for line in courses:
        clean_line = line.strip()
        parts = clean_line.split(",")

        name = parts[0]
        grade = float(parts[1])
        print(f"{name}")
        print(f"Grade: {grade}")
        print(f"{name} - Grade: {grade}")