print("hello world")
number = int(input("enter a number: "))

if number % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")

number = 5
if number:
    print("This number is truthy")

text = "hello"
if text:
    print("This string has content (truthy).")

zero = 0
if not zero:
    print("Zero is considered falsy.")

empty_text = ""
if not empty_text:
    print("This string is empty (falsy).")

level = 12
has_gear = True
health = 70

if level >= 10 and health >= 50 and has_gear:
    print("you're ready for battle!")
elif level >= 10 and health >= 50 and not has_gear:
    print("You need a weapon to fight!")
elif level >= 10 and health < 50:
    print("Heal up before the fight!")
else:
    print("level up before entering this area.")

level = int(input("Enter your level: "))
health = int(input("Enter your health: "))
weapon_input = input("Do you have a weapon? (yes/no): ")

has_gear = weapon_input.lower() == "yes"

if level >= 10 and health >= 50 and has_gear:
    print("you're ready for battle!")
elif level >= 10 and health >= 50 and not has_gear:
    print("You need a weapon to fight!")
elif level >= 10 and health < 50:
    print("Heal up before the fight!")
else:
    print("level up before entering this area.")

level = 12
has_gear = True
has_armor = False
health = 70
has_magic_ring = True

if level >= 10 and health >= 50 and (has_gear or has_armor):
    print("you're ready for battle!")

elif level >= 10 and health >= 50 and not (has_gear or has_armor):
    print("You need a weapon or armor to fight!")

elif level >= 10 and health < 50:
    print("Heal up before the fight!")

elif has_magic_ring:
    print("The ring grants you access!")

print(list(range(1,5,2)))

for num in range(1, 6):
    print(f"The current number is {num}.")

for i in range(5):
    print(i)

for i in range(10,0,-2):
    print(i)

count = 10
while count >= 0:
    print(count)
    count -= 1
print("Rocket blasting")

i = 1
while i <= 3:
    print(i)
    i += 1

x = 1 
while x < 10:
    x *=2
    print(x)

for row in range(3):
    for col in range(4):
        print("*",end=" ")
    print() # New Line after each row
  
for i in range(1, 5):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

for i in range(1, 5):
    for col in range(1, row + 1):
        print(col, end=" ")
    print()