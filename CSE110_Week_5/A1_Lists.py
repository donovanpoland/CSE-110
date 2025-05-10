
name = ""
friends = []
while name.lower() != "end":
    name = input("What are the names of your freinds? ")
    if name.lower() != "end":
        friends.append(name.capitalize())

print("Your friends are: ")
for friend in friends:
    print(friend)


#harder way of doing it.
# for friend in friends:
#     if friend == "end":
#         friend = ""
#     else:
#         friend
#         print(f"Your freinds are: {friend}")