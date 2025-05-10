lowest_life_exp = float('20000')
highest_life_exp = float('-1')
lowest_country = highest_country = lowest_year = highest_year = ""
min_life_exp_year = float('20000')
max_life_exp_year = float('-1')
min_country = max_country = single_country = ""
earliest_year = float('20000')
latest_year = float('-1')

total_life_exp = num_of_years = 0
available_years = set()

# First pass: Determine earliest and latest year
with open("life-expectancy.csv") as life_expectancy_list:
    # Skip header
    next(life_expectancy_list)  
    for line in life_expectancy_list:
        # Extract year from each line
        year = int(line.split(",")[2])  

        earliest_year = min(earliest_year, year)
        latest_year = max(latest_year, year)
        available_years.add(year)  # Store unique years

# Loop until a valid year is provided
while True:
    try:
        chosen_year = int(input(f"(Between {earliest_year} and {latest_year}) Enter the year to find the average life expectancy for: "))
        if chosen_year in available_years:
            break
        print(f"Data is not available for {chosen_year}. Please enter a valid year.")
    except ValueError:
        print("Invalid input. Please enter a valid year.")

# Process data for chosen year and overall extremes
with open("life-expectancy.csv") as life_expectancy_list:
    next(life_expectancy_list)
    for line in life_expectancy_list:
        data_set = line.strip().split(",")
        country, year, life_exp = data_set[0], int(data_set[2]), float(data_set[3])

        if year == chosen_year:
            total_life_exp += life_exp
            num_of_years += 1
            single_country = single_country or country  # Track if only 1 country is found

            # Update min and max life expectancy for chosen year
            if life_exp < min_life_exp_year:
                min_life_exp_year, min_country = life_exp, country
            if life_exp > max_life_exp_year:
                max_life_exp_year, max_country = life_exp, country

        # Update global min and max life expectancy
        if life_exp < lowest_life_exp:
            lowest_life_exp, lowest_country, lowest_year = life_exp, country, year
        if life_exp > highest_life_exp:
            highest_life_exp, highest_country, highest_year = life_exp, country, year

# Calculate and display the average life expectancy for the chosen year
if num_of_years:
    average_life_exp = round(total_life_exp / num_of_years, 2)
    if num_of_years == 1:
        print(f"\nWorldwide limited data: life expectancy for {chosen_year} in {single_country} was {average_life_exp}")
    else:
        print(f"\nFor {chosen_year}:\nAverage Life Expectancy: {average_life_exp}")
        print(f"Maximum Life Expectancy: {max_life_exp_year} in {max_country}")
        print(f"Minimum Life Expectancy: {min_life_exp_year} in {min_country}")
else:
    print(f"\nNo data available for {chosen_year}.")

# Display global life expectancy extremes
print(f"\nHighest life expectancy worldwide: {highest_life_exp} in {highest_country} ({highest_year})")
print(f"Lowest life expectancy worldwide: {lowest_life_exp} in {lowest_country} ({lowest_year})")
