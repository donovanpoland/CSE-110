

numbers = []
user_input = 1
sum = 0
average = 0
largest = 0
smallest_positive = None


while user_input != 0:
    user_input = float(input("Enter a list of numbers, type 0 when finished. "))
    if user_input != 0:
        numbers.append(user_input)
      
smallest = numbers[0]

#testing
print(numbers)

#calculate the sum
for number in numbers:
    sum += number
print(f"The sum is {sum}")

#find the average
average = sum / len(numbers)
print(f"The average is {average}")

#find the largest number
for number in numbers:
    if number >= largest:
        largest = number
print(f"The largest nubmer is {largest}")



for number in numbers:
    #find the smallest number
    if number < smallest:
        smallest = number
    #find the smallest positive number
    if number > 0 and (smallest_positive is None or number < smallest_positive):
         smallest_positive = number


print(f"\nThe smallest nubmer using a for loop {smallest}")

print(f"The smallest positve nubmer is {smallest_positive}")


alt_smallest_number = min(numbers)
print(f"\nUsing 'min' function {alt_smallest_number}")

#sort numbers
sorted_list = sorted(numbers)
print("The list sorted is:")
for i in sorted_list:
    print(i)