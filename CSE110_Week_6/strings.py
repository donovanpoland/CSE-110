# This is a single string
colors = "Red Green Blue Yellow"

# default is " ", it splits the string at the space
color_parts = colors.split()

print(colors)
print(color_parts)

for color in color_parts:
    print(color)

second = color_parts[1]
print(f"The second color is: {second}")

color_parts = colors.split("e")
print(color_parts)

colors_comma = "Red,Green,Blue,Yellow"
color_parts = colors.split(",")
print(color_parts)