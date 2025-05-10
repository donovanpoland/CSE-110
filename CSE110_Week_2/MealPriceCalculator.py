#creativity
"""
Added an if statement to change the output depending on if they user under pays for the total bill and converts the number from negative to positive for display purposes
"""

#instructions
"""
Compute the price of a meal as follows by asking for the price of child and adult meals, the number of each, and then the sales tax rate.
Use these values to determine the total price of the meal. Then, ask for the payment amount and compute the amount of change to give back to the customer.
Keep in mind that some of these values are floating point numbers (they can have decimals) and some of them are integers (whole numbers).

Ask the user for the following:
    >The price of a child's meal (floating point)
    >The price of an adult's meal (floating point)
    >The number of children (integer)
    >The number of adults (integer)
Then, complete the following steps:
    >Determine the meal's subtotal (before adding sales tax) by multiplying the number of children by the price of their meal,
        and multiplying the number of adults by the price of their meal and adding those two values together.
    >Display the subtotal.
    >Ask the user for the sales tax rate as a percentage (floating point). 
        Please note that this percentage should be entered and stored as a number such as 6, or 6.5, not 0.06 or 0.065.
    >Compute and display the sales tax, by multiplying the subtotal by the sales tax rate divided by 100.
    >Compute and display the total price of the meal by adding the subtotal and the sales tax.
Finally:
    >Ask the user for the the payment amount (floating point)
    >Compute and display the change.
"""

#ask user for price of a child's meal, adults meal, number of children and number of adults
child_price = float(input("What is the price of a child's meal? "))
adult_price = float(input("What is the price of a adult's meal? "))
children = int(input("How many children are there? "))
adults = int(input("How many adults are there? "))

#tests
# child_price = 4.99999
# adult_price = 10.9999
# children = 6
# adults = 10
# tax_percent = 6.99999
# payment = 150

#calculate subtotal and display and format to 2 decimals
subtotal = (child_price * children) + (adult_price * adults)
print(f"\nSubtotal: ${subtotal:.2f}")

#ask usre for sales tax rate
tax_percent = float(input("What is the sales tax rate? "))
#calculate tax and display and format to 2 decimals
sales_tax = subtotal * (tax_percent / 100)
print(f"Tax: ${sales_tax:.2f}")
#calculate total and display and format to 2 decimals
total = subtotal + sales_tax
print(f"Total: ${total:.2f}")

#ask for payment, calculate and display left over change and format to 2 decimals
payment = float(input("how much is your payment amount? "))
change = payment - total
negative = -1
#if payment is less than total dispplay that the user still owes money or give remaining change
#convert negative number if change is oweed to positive for display purposes us abs function
print(f"You still owe: ${abs(change):.2f}") if payment < total else print(f"Change: ${change:.2f}")

