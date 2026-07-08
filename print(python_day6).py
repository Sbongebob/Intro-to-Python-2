# creating a list of string
fruits = ["apple", "banana", "cherry",]
print(fruits)

#creating a list of number

# Adding elements
fruits.append("orange")
print(fruits)


fruits.insert(1, "blueberry")
print(fruits)

# removing elemnts
fruits.remove("banana")
print(fruits)

#popping elements (removes and returns the last elemetn by default)
last_fruits = fruits.pop()
print(last_fruits)
print(fruits)

colors = ["red", "blue", "green", "yellow", "purple"]
fruits = ["apple", "banana", "cherry"]

fruits.append("orange")
print(fruits)

fruits.remove("banana")
print(fruits)
#advanced: reverse the list and print it
numbers = [1, 2, 3, 4, 5, 6]
print(numbers[1:4]) #output: [2, 3, 4]
print(numbers[:3]) #output: [1,2,3]
print(numbers[3:]) #output: [4, 5, 6]
print(numbers[-3:]) #output: [4, 5, 6]

# Lists
colors = ["red", "blue", "green", "yellow", "purple"]
fruits = ["apple", "banana", "cherry"]

# Add an item
fruits.append("orange")
print(fruits)

# Remove an item
fruits.remove("banana")
print(fruits)

# Advanced: Reverse the list and print it
fruits.reverse()
print(fruits)

# List slicing
numbers = [1, 2, 3, 4, 5, 6]
print(numbers[1:4])   # Output: [2, 3, 4]
print(numbers[:3])    # Output: [1, 2, 3]
print(numbers[3:])    # Output: [4, 5, 6]
print(numbers[-3:])   # Output: [4, 5, 6]

# Use slicing to print the first three elements
Number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print(Number[:3])     # Output: [1, 2, 3]

# Advanced: Use a loop to print all even numbers
print("Even numbers:")
for num in Number:
    if num % 2 == 0:
        print(num)

# Sort the list in ascending order
Marks = [87, 45, 78, 92, 66]
Marks.sort()
print("Sorted marks:", Marks)

import statistics

# Advanced: Calculate and print the average
average = sum(Marks) / len(Marks)
print("Average:", average)