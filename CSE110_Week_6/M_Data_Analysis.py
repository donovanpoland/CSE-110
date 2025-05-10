"""
I show the user the lowest year and the highest year of data available and display output
If there is only 1 year you are told there is limited date for that year.
If there are no years in the data that match the user input then repeat.
Along side the average life expectancy I also find the maximum and minimum life expectancy across all countrys for the chosen year
"""


lowest_life_exp = float('20000')  
highest_life_exp = float('-1')  
lowest_country = ""
lowest_year = ""
highest_country = ""
highest_year = ""
min_life_exp_year = float('20000')
max_life_exp_year = float('-1')
min_country = ""
max_country = ""
earliest_year = float('20000')
latest_year = float("-1")
single_country = ""

total_life_exp = 0
num_of_years = 0
available_years = set()


# First pass: Determine earliest and latest year
with open("life-expectancy.csv") as life_expectancy_list:
    # Skip the header
    next(life_expectancy_list)  

    for line in life_expectancy_list:
        clean_line = line.strip()
        data_set = clean_line.split(",")
        year = int(data_set[2])

        # Update earliest and latest year
        if year < earliest_year:
            earliest_year = year
        if year > latest_year:
            latest_year = year

        # Add year to the set of available years
        available_years.add(year)

# Loop until a valid year is provided
while True:
    try:
        # Ask the user for a year
        chosen_year = int(input(f"(Between {earliest_year} and {latest_year}) Enter the year you want to find the average life expectancy for: "))
        
        # Check if the chosen year is in the set of available years
        if chosen_year not in available_years:
            print(f"Data is not available for the year {chosen_year}. Please enter a valid year.")
            # Prompt again
            continue  
        # Exit loop if valid year is entered
        break  
    except ValueError:
        print("Invalid input. Please enter a valid year.")

# Open life expectancy file and close when done
with open("life-expectancy.csv") as life_expectancy_list:
    # Skip the header
    next(life_expectancy_list)

    # Clean up the lines, split the file by commas and asign values to the data
    for line in life_expectancy_list:
        clean_line = line.strip()
        data_set = clean_line.split(",")
        country = data_set[0]
        code = data_set[1]# unused
        year = int(data_set[2])
        life_exp = float(data_set[3])

        # Check for the user chosen year and calculate the total and count the number of years to find the average later on
        if year == chosen_year:
            #if there is only 1 country store the name for that year
            single_country = country
            total_life_exp += life_exp
            num_of_years += 1

             # Update minimum and maximum life expectancy for the chosen year
            if life_exp < min_life_exp_year:
                min_life_exp_year = life_exp
                min_country = country
            if life_exp > max_life_exp_year:
                max_life_exp_year = life_exp
                max_country = country

        # Check for lowest life expectancy
        if life_exp < lowest_life_exp:
            lowest_life_exp = life_exp
            lowest_country = country
            lowest_year = year

        # Check for highest life expectancy
        if life_exp > highest_life_exp:
            highest_life_exp = life_exp
            highest_country = country
            highest_year = year


# Calculate the average life expectancy for the user-specified year and round to the second decimal place
average_life_exp = round((total_life_exp / num_of_years), 2)
# If there is only 1 year of data available
if num_of_years == 1:
    print(f"\nWorld wide there is limited data, the life expectancy for {chosen_year} in {single_country} was {average_life_exp}")
elif num_of_years > 1:
    print(f"\nFor the year {chosen_year}:")
    print(f"The average life expectancy across all countries was {average_life_exp}")
    print(f"The maximum life expectancy was {max_life_exp_year:.3f} in {max_country} {chosen_year}")
    print(f"The minimum life expectancy was {min_life_exp_year:.3f} in {min_country} {chosen_year}")
else:
    print(f"\nNo data available for the year {chosen_year}.")

# Display lowest and highest life expectancy
print(f"\nHighest life expectancy world wide was {highest_life_exp} in {highest_country} {highest_year}")
print(f"Lowest life expectancy world wide was {lowest_life_exp} in {lowest_country} {lowest_year}")