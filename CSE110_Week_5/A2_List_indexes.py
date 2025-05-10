

item = ""
shopping_cart = []

print("\nPlease enter the items of the shopping list (type: quit to finish) :")
while item.lower() != "quit":
    item = input("Item: ")
    if item.lower() != "quit":
        shopping_cart.append(item.capitalize())

print("\nThe shopping list is: ")
for item_in_list in shopping_cart:
    print(item_in_list)

print("\nThe shopping list with indexes is: ")
for i in range(len(shopping_cart)):
    temp_item = shopping_cart[i]
    print(f"{i}. {temp_item}")

index = int(input("Which index item would you like to change? "))

# Update the selected index with the new item
item = input("What is the new item? ")
shopping_cart[index] = item.capitalize()

print("\nThe shopping list with indexes is: ")
for i in range(len(shopping_cart)):
    temp_item = shopping_cart[i]
    print(f"{i}. {temp_item}")