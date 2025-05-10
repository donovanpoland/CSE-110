# Creativity
"""
I had to learn so many new things to build this program, I tried realy hard to find every bug and every conditon and used "try" and "except"s to prevent invalid user input,
I learned beter ways to make infinte loops, and how to use 'continue' and 'break' to do things over or end the loop,
My creativity portion was to add coupons to allow for a discount to be applied to the cart when calculated,
I had troubles with removing the other itmes and leaving the coupons available in my shopping cart, it would create negative calculations so I had to check for negatives in each menu option,
I relized later i could have just checked once when in the menue itself instead of all the menu options,
I then realized I didnt need that anymore if I just make the coupons expire when an item was removed since the coupon avialability was based on the subtotal 
If I had more time I would rewrite this program with a seperate list holding the coupons and use some math functions instead of loops to do alot of the math involved.
.....370 lines of code later here you go. It was fun but so hard. Good luck breaking it. There are probably still some bugs but I don't have any more time to find/fix them.
"""

# Declare variables
menu = True
shopping_cart = []
prices = []
number_of_discounts = 0



# Testing cart
# shopping_cart = ["milk", "cookies", "cup", "cup", "plate"]
# prices = [1.99, 2.99, 1.00, 1.00, 1.50]

# Initial welcome and enter menu loop
print("\nWelcome to the Shopping Cart Program!")
# Menu == True 
while menu:

    # Print the menu
    print("\nPlease select one of the following:\n" + 
          "1. Add Item\n" + 
          "2. View Cart\n" + 
          "3. Remove Item\n" + 
          "4. Coupons\n" +
          "5. Compute Total\n" + 
          "6. Quit")
    
    # Print list for testing
    # print(shopping_cart)
    # print(prices)

    # Request an option from the user
    option = input("Please enter an action: ")

        # If option 1 is chosen add items to cart
    if option == "1" or option.lower() == "add item":
        
        # Ask how many items the user wants to add
        while True:
            try:
                num_items = int(input("\nHow many items would you like to add? "))
                if num_items <= 0:
                    print("Please enter a positive number.")
                     # Prompt for number again
                    continue
                # Exit the loop when valid price is entered 
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        
        # Add the number of items specified by the user
        # Index not used in loop
        for _ in range(num_items):
            item = input("\nWhat item would you like to add? ").strip()
            
            # Ensure the item is not just empty space
            if item == "":
                print("You need to enter an item.")
                # Ask for the item again
                continue  
            
            # Loop for ensuring price input is valid
            while True:
                try:
                    price = float(input(f"What is the price for {item}? "))
                    # Check if the price is positive
                    if price <= 0:
                        print("Please enter a positive number for the price.")
                        # Prompt for price again
                        continue 
                    # Exit the loop when valid price is entered 
                    break  
                except ValueError:
                    print("Invalid input. Please enter a valid number for the price.")
        
            # Add the item and price to the lists
            shopping_cart.append(item.title())
            prices.append(price)
        
        # Let the user know the process is finished
        print("\nAll items have been added to your cart.")
        # Return to the main menu after adding items
        continue
                      
    # View cart option
    elif option == "2" or option.lower() == "view cart":

        # Check if the 'shopping cart' aka prices[] is empty or only has coupons
        # If it has positive values its not empty if it only has negative values its empty
        non_coupon_items = []
        for price in prices:
            if price > 0:
                non_coupon_items.append(price)

         # If lists are not empty, continue
        if len(non_coupon_items) > 0:
                print("\nYour shopping cart is:")
                for i in range(len(shopping_cart)):
                    temp_item = shopping_cart[i]
                    temp_price = prices[i]
                    print(f"{i + 1}. {temp_item.title()} - ${temp_price:.2f}")
        else:
            # List(s) is empty so remove coupons
            shopping_cart.clear()
            prices.clear()
            print("\nYour cart is empty!")
            
        # Block the loop from ending and puting user back into menu so the shopping cart can be viewed without interuption
        exit_to_menu = False
        while exit_to_menu == False:        
            # Ask if the user wants to add more items
            again = input("\nWould you like to go back to the menu? (yes/no): ").strip().lower()
            if again == "yes":
                exit_to_menu = True

    # Remove item option
    elif option == "3" or option.lower() == "remove item":

        # Reset done for the remove item loop
        exit_to_menu = False

        # Check if the 'shopping cart' aka prices[] is empty or only has coupons
        # If it has positive values its not empty if it only has negative values its empty
        non_coupon_items = []
        for price in prices:
            if price > 0:
                non_coupon_items.append(price)

        # If lists are empty, continue
        if len(non_coupon_items) > 0:
            if len(shopping_cart) > 0:
                removing = False
                # Display shopping cart to user
                while removing == False:
                    print("\nYour shopping cart is:")
                    for i, item in enumerate(shopping_cart, 1):
                        print(f"{i}. {item.title()} - ${prices[i-1]:.2f}")

                    # Get item to remove
                    remove_item = input("Enter the name or the number in list of the item you'd like to remove (or type 'Done' to stop): ")

                    # Exit the remove loop and go back to menu
                    if remove_item.lower() == "done":
                        removing = True  

                    # Remove by index
                    elif remove_item.isdigit() and 1 <= int(remove_item) <= len(shopping_cart):
                        # Convert to zero-based index
                        index = int(remove_item) - 1
                        removed_item = shopping_cart.pop(index)
                        removed_price = prices.pop(index)
                        print(f"\n{removed_item.title()} has been removed from your cart. Price was: ${removed_price:.2f}")
                        # Remove the coupon from both shopping_cart and prices lists
                        # Iterate over the shopping_cart by index in reverse order to safely remove items
                        for i in range(len(shopping_cart) - 1, -1, -1):
                            if shopping_cart[i].lower() == "coupon":
                                shopping_cart.pop(i)
                                prices.pop(i)
                                print("Your coupon expired.")
                    
                    # Remove by name
                    elif remove_item.title() in shopping_cart:
                        index = shopping_cart.index(remove_item.title())
                        removed_item = shopping_cart.pop(index)
                        removed_price = prices.pop(index)
                        print(f"{removed_item.title()} has been removed from your cart. Price was: ${removed_price:.2f}")
                        # Remove the coupon from both shopping_cart and prices lists
                        # Iterate over the shopping_cart by index in reverse order to safely remove items
                        for i in range(len(shopping_cart) - 1, -1, -1):
                            if shopping_cart[i].lower() == "coupon":
                                shopping_cart.pop(i)
                                prices.pop(i)
                                print("Your coupon expired.")

                    else:
                        print("That item is not in your cart.")
            else:
                print("\nYour cart is empty!")
        else:
            # The lists are empty, remove coupons
            shopping_cart.clear()
            prices.clear()
            print("\nYour cart is empty!")
            
        # Block the loop from ending and puting user back into menu so the receipt can be viewed without interuption
        exit_to_menu = False
        while exit_to_menu == False:   
            # Ask if the user wants to add more items
            again = input("\nWould you like to go back to the menu? (yes/no): ").strip().lower()
            if again == "yes":
                exit_to_menu = True

    # Coupon option
    elif option == "4" or option.lower() == "coupon" or option.lower() == "coupons":
        exit_to_menu = False
        
        # Check if the 'shopping cart' aka prices[] is empty or only has coupons
        non_coupon_items = []
        for price in prices:
            if price > 0:
                non_coupon_items.append(price)

        # Lists not empty, continue
        if len(non_coupon_items) > 0:
            exit_to_menu = False

            # Calculate subtotal of the current shopping cart
            subtotal = 0
            for price in prices:
                if price > 0:
                    subtotal += price

                    # Calculate total discounts
            total_discount_price = 0
            for price in prices:
                if price < 0:
                    total_discount_price += price

            # Set the maximum discount to 25% of the subtotal
            max_discount_allowed = subtotal * 0.25
            # If max discount does not get rounded you can get stuck int he loop
            round(max_discount_allowed, 2)

            print(f"\nTotal Discounts: ${abs(total_discount_price):.2f}")
            print(f"Total Discounted Items: {number_of_discounts}")

            if number_of_discounts < 5:
                print(f"\nYour current subtotal is: ${subtotal:.2f}")
                # Testing
                #print(f"Maximum Discount Applicable: ${max_discount_allowed}")
                print(f"Maximum Discount Applicable: ${max_discount_allowed:.2f}")
   

            while exit_to_menu == False:
                # Calculate the available amount to discount
                available_discount = (max_discount_allowed + total_discount_price)

                # If no discount is available or to many discounts too are added, break the loop
                if available_discount <= 0 or number_of_discounts >= 5:
                    print("\nNo further discounts can be applied.")
                    break

            
                # Loop for ensuring valid discount input
                while True:
                    try:
                        
                        print(f"Remaining Discounts: {5 - number_of_discounts}")
                        # Testing
                        #print(f"Remaining Amount: ${available_discount}")
                        round(available_discount)
                        print(f"Remaining Amount: ${available_discount:.2f}")
                        discount = float(input("How much is the discount? (negative value) "))
                        if discount >= 0:
                            print("Please enter a negative number for the discount.")
                            continue
                        elif abs(discount) > available_discount:
                            print("That discount is not possible. It exceeds the remaining subtotal.")
                            continue  # Prompt again

                        # If valid discount, exit the loop
                        break

                    except ValueError:
                        print("Invalid input. Please enter a valid number for the discount.")

                # Apply the valid discount
                shopping_cart.append("Coupon")
                prices.append(discount)
                # Update total discounts after adding
                total_discount_price += discount  
                # Calculate the available amount to discount
                available_discount = (max_discount_allowed + total_discount_price)
                number_of_discounts += 1
                    
                # Ask if the user wants to add more items
                if available_discount > 0:
                    again = input("Would you like add another coupon? (Yes/No): ").strip().lower()
                    if again != "yes":
                        exit_to_menu = True
                else:
                    print("No further discounts can be applied.")
                    exit_to_menu = True

        else:
            #list is empty so remove coupons
            shopping_cart.clear()
            prices.clear()
            print("\nYour cart is empty!")

    # Compute total option
    elif option == "5" or option.lower() == "compute total" or option.lower() == "total":

        no_negagive_totals = 0
        # Create a new list of prices without negative values
        adjusted_prices = []
        for price in prices:
            if price > 0:
                adjusted_prices.append(price)
            else:
                no_negagive_totals += price

        # Check if the shopping cart is empty or if only negative numbers(coupons) are in the shoping cart
        if len(adjusted_prices) > 0:
                # Calculate subtotal (sum of positive prices only, i.e., before discounts)
                subtotal_before_discounts = 0
                for price in prices:
                    if price > 0:
                        subtotal_before_discounts += price

                # Calculate total discounts (sum of negative prices)
                total_discounts = no_negagive_totals
                

                # Calculate the tax rate (6%)
                tax_rate = 6 / 100

                # Calculate tax based on the subtotal after discounts
                subtotal_after_discounts = subtotal_before_discounts + total_discounts  # Discounts are negative, so this effectively subtracts them
                tax_amount = subtotal_after_discounts * tax_rate  # Calculate tax amount

                # Compute the final total (subtotal after discounts + tax)
                final_total = subtotal_after_discounts + tax_amount

                print("\n--- Receipt ---\n")
                # Display items in shopping cart
                for i in range(len(shopping_cart)):
                    temp_item = shopping_cart[i]
                    temp_price = prices[i]
                    print(f"{i + 1}. {temp_item.title()} - ${temp_price:.2f}")
                # Display all amounts
                print(f"\nSubtotal: ${subtotal_before_discounts:.2f}")
                print(f"Discounts: ${total_discounts:.2f}")
                print(f"New Subtotal: ${subtotal_after_discounts:.2f}")
                print(f"Applicable Tax: ${tax_amount:.2f}")
                print(f"Total Amount Due: ${final_total:.2f}")
                print("\n--- Receipt ---")

        else:
            print("\nYour cart is empty!")
            exit_to_menu = True

        # Block the loop from ending and puting user back into menu so the receipt can be viewed without interuption
        exit_to_menu = False
        while exit_to_menu == False:
                
            # Ask if the user wants to add more items
            again = input("\nWould you like to go back to the menu? (yes/no): ").strip().lower()
            if again == "yes":
                exit_to_menu = True
        

    # Quit option (end loop)
    elif option == "6" or option.lower() == "quit":
        #set menu to false and end the loop
        print("Thank you. Goodbye.")
        menu = False

    #option not listed
    else:
        print("That is not a valid option, Please try again")