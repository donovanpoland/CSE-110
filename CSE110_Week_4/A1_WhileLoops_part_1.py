


#convert to int
positive = int(input("Please enter a positive number: "))

while positive < 0:
    print("Sorry, that is a negative number. Please try again.")
    positive = int(input("Please enter a positive number: "))

print(f"Correct, {positive} is a positive number.")