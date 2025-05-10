

# list syntax
natural_list = list()

# short form
s_list = []

# list with strings
list_of_strings = ["string0", "string1", "string2"]

# list with numbers
list_of_nums = [1, 2, 3, 4, 5]

# mixed list, you shouldn't do this as it makes your code hard to work with at times
mix_list = ["name", 23, 2001]

# adding items to the end of a list
list_of_books = []

list_of_books.append("1 Nephi")
list_of_books.append("2 Nephi")
list_of_books.append("Jacob")
list_of_books.append("Enos")

#print each book in list of books
print("Your books are:")
for each_book in list_of_books:
    print(each_book)

#print the index location of each book
for index in range(len(list_of_books)):
    book = list_of_books[index]
    print(f"{index}. {book}")

# working with lists of numbers
receipts = [12.24, 18.50, 4.99, 21.75]

running_total = 0

for receipt in receipts:
    # long form
    # running_total = running_total + receipt
    # short form
    running_total += receipt
    # Display the total
print(f"The total is: {running_total:.2f}") # This displays: The total is: 57.48

#this behaves differently when you do =+
#this will ad the price of receipt to running total and reset it every time as the + after = is actually saying +receipt and does not interact with the = sign
#this will display the last price of the receipt as the running total sence it was replaced every time
#adding + infront of a number or vaiable will make the number positive
for receipt in receipts:
    running_total =+ receipt

# Display the total
print(f"The total is: {running_total:.2f}") # This displays: The total is: 21.75