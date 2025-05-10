"""
It didn't make sense to ask for Celsius, convert it to Fahrenheit, and then display the conversion—especially if the user might not be familiar with Fahrenheit. 
Instead, I calculated the wind chill in Fahrenheit, then displayed both Celsius and Fahrenheit for temperatures and wind speeds, 
converting the wind chill back to Celsius so it's easier for the user to understand.
"""

# T = Air Tempature (F/C)
# V = Wind Speed (mph/kmh)
# Wind Chill formula (Fahrenheit) = 35.74 + 0.6215T - 35.75(V ** 0.16) + 0.4275T(V ** 0.16)

# Wind Speed
ws = 5

temp = float(input("What is the tempature? "))
metric = input("Fahrenheit or Celsius (F/C)? ")
# Convert metric for later use
metric = metric.upper()

# Calculate windspeed formula so it doesnt need to be calculated every time
def calc_ws(ws):
    ws = ws ** 0.16
    return ws

# Calculate windchill fahrenheit
def calc_windchill_f(temp, ws):
    wind_chill = 35.74 + 0.6215 * temp - 35.75 * (calc_ws(ws)) + 0.4275 * temp * (calc_ws(ws))
    return wind_chill

# Convert celsius to fahrenheit
def c_to_f(temp):
    f = temp * 9 / 5 + 32
    return f

# Convert Fahrenheit to Celsius
def f_to_c(temp):
    c = (temp - 32) * 5 / 9
    return c

# Convert mph to kmh
def mph_to_kmh(ws):
    ws = ws * 1.6093440
    return ws

# Calculate celcius tempature after converting to fahrenhiet
def calc_windchill_c(temp, ws):
    temp_in_f = c_to_f(temp)
    # Calculate windchill in Fahrenheit
    windchill_f = calc_windchill_f(temp_in_f, ws)
    # Convert windchill back to Celsius
    windchill_c = f_to_c(windchill_f)
    # Return both units
    return windchill_f, windchill_c
    
# Loop until wind speed exceeds the limit
while True:
    if metric.lower() == "f":
        print(f"At temperature {temp:.2f}{metric}, and wind speed {ws}mph, the windchill is: {calc_windchill_f(temp, ws):.2f}F")
        # Inciment wind chill by 5
        ws += 5
    elif metric.lower() == "c":
        windchill_f, windchill_c = calc_windchill_c(temp, ws)
        print(f"At temperature {temp:.2f}{metric}/{c_to_f(temp):.2f}F, and wind speed {mph_to_kmh(ws):.2f}kmh/{ws}mph, the windchill is: {windchill_c:.2f}C/{windchill_f:.2f}F")
        # Inciment wind chill by 5
        ws += 5
    else:
        print("That is not a valid metric for temperature.")
        metric = input("Fahrenheit or Celsius (F/C)? ")
        # Convert metric for later use
        metric = metric.upper()
    
    # Break loop after wind speed is 60
    if ws > 60:
        break
    
    