
# instructions
"""
    Each team activity will contain three core requirements.These are items that you are expected to be able to complete during the one hour team meeting if you have come prepared.

    Core Requirements
    You should work through the assignment in this order:

        1. Prompt for all of the necessary values and store them in variables. 
           Then display each item to the screen, without worrying about any spacing, punctuation, or formatting yet.
        2. Arrange the display so that the spacing and punctuation exactly match the example shown.
        3. Use the built-in string functions to make the last name display in all caps, the job title display in "title case," and the email display in all lowercase.
"""

# stretch chalange
"""
    The stretch challenges for this activity are:

    1. Add hair color and eye color and put them both on the same line in the display.
    2. Add a field for the name of the month they started and also a yes/no field for whether they have completed advanced training.
       Put these both on the same line in the display.

    3. For the two lines that you just added, make it so that the second columns align, regardless of how many letters are in the responses.
       To complete this one, you may need to search the internet for something like, "python spacing format" or something similar to see if you get any ideas.
"""

print("Please enter each feild as prompted below.")
# ask user for information
f_name = input("First name: ")
l_name = input("Last name: ")
email = input("Email address: ")
phone_number = input("Phone number: ")
job_title = input("Job title: ")
id_number = input("ID number: ")

# ask for additonal information
eye_color = input("Eye color: ")
hair_color = input("Hair color: ")
start_month = input("Start month: ")
adv_training = input("Advanced training? (yes/no): ")


# for testing
# f_name = "donovan"
# l_name = "poland"
# eye_color = "brown"
# hair_color = "brown"
# email = "Test@EMAIL.COM"
# phone_number = "801-NUM-NUMB"
# job_title = "LEAD PROGRAMMER"
# start_month = "SEPTEMBER"
# adv_training = "YES"
# id_number = "86-75309"

# extra characters for length testing (copy/paste) --> 123456789101112131415161718192021222324252627282930
# count number of characters/spaces in start_month and hair_color to use in formating and spacing
"""solves conditon: 'regardless of how many letters are in the responses.' """
num_of_char1 = len(start_month) + 1
num_of_char2 = len(hair_color)

# format input
f_name = f_name.capitalize()
l_name = l_name.upper()
job_title = job_title.title()
email = email.lower()
hair_color = hair_color.capitalize()
start_month = start_month.capitalize()
eye_color = eye_color.capitalize()
adv_training = adv_training.capitalize()


# print ID card
print("\nThe Id Card is:\n" +
      "------------------------------------------------")
print(l_name+ ", " + f_name) 
print(job_title)
print("ID: " + id_number + "\n")
print(email)
print(phone_number + "\n")

# default spacing 25 and 24 with a contingent of moving the eye_color and adv_training if the nubmer of charactors
print(f"Hair: {hair_color.ljust(num_of_char1):25} Eyes: {eye_color}     ")
print(f"Month: {start_month.ljust(num_of_char2):24} Training: {adv_training}")
print("------------------------------------------------")