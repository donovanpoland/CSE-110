#instructions
"""
Activity Instructions
    For this activity, you will implement a simplistic system to determine if a user can qualify for a loan.

The Problem: Qualifying for a loan
    When loaning money to someone, you want to have some level of confidence that they will be able to repay the loan.

    There are different characteristics you might base this decision on, or different questions you might ask someone.
    And depending on their answers to those questions, you might ask other questions. For example, consider the following possible questions:

        >Does the person have a job, and if so, how long have they worked there, and how much money do they make?
        >Is there good collateral for the loan? (for example, is the loan against a car or home that is worth at least the amount of the loan?)
        >Does the person have a good credit score or history of paying back loans?
        >How much other debt does the person have?
        >How much money does the person have?
        >Will the person have a down payment, and if so, what percentage of the loan does it amount to?

Program Specification
    Write a program to determine whether to loan money based on the following rules.

    First, ask for a rating from 1-10 on the following:

        >How large is the loan?
        >How good is your credit history?
        >How high is your income?
        >How large is your down payment?

    Then, you will create a boolean variable for whether you should loan the money that will be set to either True or False. 
    Set up a series of if statements to decide if your decision to loan is "yes" or "no" according to the following rules:

        >First, check if the loan size is at least 5. If it is, use the following rules:
            >If the credit history and income are both at least 7, then the decision is "yes"
            >If either the credit history or income is at least 7, then check if the down payment is at least 5, if it is, the decision is "yes", if not, the decision is "no"
            >Otherwise (if neither the credit history nor income is at least 7), the decision is "no"

        >Otherwise (if the loan is not 5 or greater), use these rules:
            >If the credit is less than 4, then the decision is "no"
            >Otherwise, check the following:
                >If either the income or the down payment is at least 7, the decision is "yes"
                >If both the income and the down payment are at least 4, then the answer is "yes"
                >Otherwise, the decision is "no"

    Finally, display the decision to the user.
"""

#testing

"""
1. Loan size: 8, Credit: 7, Income: 8, Down Payment: 1, Decision: "yes"
2. Loan size: 5, Credit: 2, Income: 7, Down Payment: 5, Decision: "yes"
3. Loan size: 8, Credit: 2, Income: 8, Down Payment: 3, Decision: "no"
4. Loan size: 2, Credit: 4, Income: 1, Down Payment: 7, Decision: "yes"
5. Loan size: 4, Credit: 5, Income: 5, Down Payment: 3, Decision: "no"
"""

# Initial loan qualification status
interest = 0.01
monthly_payment = 1
years_lent = 1

# Function to check qualification
def check_qualification(condition, disqualification_message):#still need to learn what def does, i know this is a function and passing 2 values into it
    if not condition: #this is a weird if statement need to learn why this works
        print(disqualification_message)
        exit()

#ask for loan amount
loan = float(input("How much would you like to loan? "))
qualify_message = f"Congratulations you qualify for a loan of ${loan:,.2f}"

#Determin loan amount approval, interest rate and number of years available
if loan >= 1000 and loan <= 5000:
    interest = 0.1
    years_lent = 3
elif loan >= 5001 and loan <= 10000:
    interest = 0.2
    years_lent = 5
elif loan >= 10001 and loan <= 20000:
    interest = 0.3
    years_lent = 7
else:
    check_qualification(loan <= 20000, "Loan amount not available.")

#ask user if downpayment will be payed
down_payment = float(input("Will you be making a downpayment? If no please type 0, how much? "))
#new loan amount
loan = loan - down_payment

# Calculate loan payments
number_of_payments = years_lent * 12  # Total number of payments (monthly)
monthly_interest_rate = interest / 12  # Convert annual interest rate to monthly
    
# Monthly payment formula
monthly_payment = loan * monthly_interest_rate * (1 + monthly_interest_rate)**number_of_payments / ((1 + monthly_interest_rate)**number_of_payments - 1)
 
# Total payment
total_payment = monthly_payment * number_of_payments
interest_percentage = interest * 100

print("If you qualify for a loan, here is what we offer and what your payments will look like.")
print(f"Loan Amount: ${loan + down_payment:,.2f}\nInterest: {interest_percentage:.2f}%\nMonthly Payment: ${monthly_payment:,.2f}\nTotal Payment: ${total_payment:,.2f}\n")

#Does the person have a job, and if so, how long have they worked there, and how much money do they make?
job = input("Do you have a job? (Yes/no) ")
#calculate if user has a job if yes continue program if no qualify for loan = false
check_qualification(job.lower() == "yes", "Unfortunately, you do not qualify for a loan as you do not have a job.")

years_worked = int(input("How many years have you worked? "))
#calculate if user has worked for than 2 years
check_qualification(years_worked >= 2, "Unfortunately, you do not qualify for a loan as you have not worked long enough.")

earnings_per_year = float(input("How much do you earn per year? "))
gross = (earnings_per_year / 12)
tax = 0.24
net = gross - (gross * tax)
#print(f"Monthly earnings: {net:,.2f}")
max_payment = net * 0.35
#print(f"Max payment: {max_payment:,.2f}")
check_qualification(max_payment >= monthly_payment, "Unfortunately, you dont have enough income to pay this loan.")
 
#Is there good collateral for the loan? (for example, is the loan against a car or home that is worth at least the amount of the loan?)
#is collateral >= loan
collateral = input("Is the loan for a car, home construction or something else? ")
savings = float(input("Do you have savings? How much? "))
#calcuate if colateral exists
if collateral.lower == "car" or "house" or "home construction" or "construction" or "home" or "vehicle" or "motorcycle" or savings > (loan * 0.01):
    collateral = True
else:
    collateral = False

#is the user credit worthy (greater than 700)
credit = int(input("What is your credit score? (400-850) "))
#calculate credit wothyness
if loan >= 10000 and credit >= 700 or loan >= 5000 and credit >= 650 or loan <= 4999 and credit >= 600:
    credit = True
else:
    credit < 600
    print("Bad credit? No Problem. ")
    credit = False
    
#check for debt and compare to new debt added to loan and maximum allowed debt
debt = float(input("What other debt payments do you have per month? "))
check_qualification((monthly_payment + debt) <= max_payment, "Unfortunately, you have to much debt to qualify for this loan.")

#final qualifing check
check_qualification(collateral == True or credit == True or down_payment > (loan * 0.05), "Unfortunately, your credit is too low or you do not have enough colateral, or your downpayment isn't high enough."), 
print(qualify_message)





    

