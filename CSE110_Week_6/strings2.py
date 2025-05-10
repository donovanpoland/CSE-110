name = "     Donovan Poland     "
#removes all the before and after white space
clean_name = name.strip()

print(f"---{name}---")
print(f"---{clean_name}---")

name2 = "\tDonovan Poland   \n"
print(name2)
name2 = name2.strip()
print(f"{name2} test if this text goes to the next line because the name has a dashN at the end.")