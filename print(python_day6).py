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

#My way

#Practice with Tuple

# Exercise 1: Create a tuple with four school subjects
subjects = ("Math", "Science", "English", "History")

print("School subjects:")
print(subjects)

print("\nSubjects with more than five letters:")
for subject in subjects:
    if len(subject) > 5:
        print(subject)

# Exercise 2: Given tuple of animals
animals = ("cat", "dog", "rabbit", "hamster")

print("\nSecond animal:")
print(animals[1])

print("\nAnimals containing the letter 'a':")
count = 0
for animal in animals:
    if "a" in animal:
        print(animal)
        count += 1
print("Total:", count)

# Exercise 3: Try changing an item in the tuple
print("\nTrying to change a tuple item:")
try:
    animals[1] = "lion"
except TypeError:
    print("Error: Tuples cannot be changed because they are immutable.")

# Convert tuple to a list, modify it, then convert it back to a tuple
animal_list = list(animals)
animal_list[1] = "lion"
animals = tuple(animal_list)

print("Modified tuple:")
print(animals)

# Exercise 4: Print how many items are in a tuple
colors = ("red", "blue", "green", "yellow", "purple")

print("\nNumber of items in the colors tuple:")
print(len(colors))

# Advanced: Create a tuple of 10 favorite numbers
numbers = (12, 45, 7, 23, 89, 34, 56, 2, 99, 18)

print("\nFavorite numbers:")
print(numbers)

print("Maximum number:", max(numbers))
print("Minimum number:", min(numbers))

#teachers_way

animals = ("cat", "dog", "rabbit", "hamster")
print(animals)
animals_list = list(animals)

student = {
    "name": "Jordan",
    "age": 13,
    "grade": "8th"
}

person = {
    "name": "Alice",
    "age": 30,
    "skills": ["python", "Data Analysis"]
}

print(person["name"])
print(person.get("age"))
print(person["skills"])

print(person)

person2 = {
    "name": "Bieti",
    "age": 15,
    "skills": ["python", "Data Analysis", "Math"]
}

print(person2["name"])
print(person2.get("age"))
print(person2["skills"])


dict_list = [person, person2]

print(dict_list)

# 1. Create a dictionary with three friends' names and birthdays
friends = {
    "Alice": "January 5",
    "Bob": "March 12",
    "Charlie": "July 20"
}

print("Friends Dictionary:")
print(friends)

# Advanced: Ask the user to input names and birthdays
friends = {}

for i in range(3):
    name = input(f"\nEnter the name of friend {i + 1}: ")
    birthday = input(f"Enter {name}'s birthday: ")
    friends[name] = birthday

print("\nUpdated Friends Dictionary:")
print(friends)

# 2. Student dictionary
student = {
    "name": "Alex",
    "grade": 8,
    "school": "Sunrise Middle"
}

# Print the student's name
print("\nStudent Name:", student["name"])

# Change the grade to 9
student["grade"] = 9

# Advanced: Add GPA
student["GPA"] = 3.8

# Add hobby
student["hobby"] = "painting"

print("\nUpdated Student Dictionary:")
print(student)

# Advanced: Remove a key-value pair using pop()
student.pop("school")

print("\nStudent Dictionary after removing 'school':")
print(student)

# 3. Person dictionary
person = {
    "name": "Ravi",
    "age": 14,
    "city": "Seattle"
}

# Print all keys and values
print("\nPerson Dictionary:")
for key, value in person.items():
    print(key, ":", value)

# Advanced: Format and print a sentence using the values
print(f"\n{person['name']} is {person['age']} years old and lives in {person['city']}.")