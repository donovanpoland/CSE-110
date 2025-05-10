people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]

youngest = people[0].split()
youngest_name = youngest[0]
youngest_age = int(youngest[1])

for person in people:
    seperate = person.split()
    name = seperate[0]
    age = int(seperate[1])

    if age < youngest_age:
        youngest_name = name
        youngest_age = age
    
    print(f"{name} is age {age}")

    

print(f"\nThe youngest is {youngest_name}, at age {youngest_age}")

