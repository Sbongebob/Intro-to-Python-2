print("🐾 **************************** 🐾")
print("  🐶🐱 Welcome to My Digital Pet! 🐉🐸.  ")
print("🐾 **************************** 🐾")

pet_name = input("🐾 Enter your pet's name: ")
pet_type = input("🦴 Enter your pet's type (dog 🐶, cat 🐱, dragon 🐉, frog 🐸, etc.): ")

hunger = 80
happiness = 80
energy = 80
health = 100
cleanliness = 80
level = 1

print("\n🎉 Your pet is ready!")
print("-------------------------")
print("📛 Name:", pet_name)
print("🐾 Type:", pet_type)
print("⭐ Level:", level)
print("🍖 Hunger:", hunger)
print("😊 Happiness:", happiness)
print("⚡ Energy:", energy)
print("❤️ Health:", health)
print("🛁 Cleanliness:", cleanliness)

while health > 0:
    print("\n====== 🐾 MENU 🐾 ======")
    print("1. 🍖 Feed")
    print("2. 🎾 Play")
    print("3. 😴 Sleep")
    print("4. 🛁 Clean")
    print("5. 🏥 Visit Vet")
    print("6. 🚪 Quit")

    choice = input("👉 Choose an option (1-6): ")

    if choice == "1":
        hunger = min(100, hunger + 20)
        health = min(100, health + 5)
        cleanliness = max(0, cleanliness - 10)
        print("🍖", pet_name, "really liked the food!")

    elif choice == "2":
        happiness = min(100, happiness + 20)
        hunger = max(0, hunger - 10)
        energy = max(0, energy - 15)
        cleanliness = max(0, cleanliness - 10)
        print("🎉", pet_name, "had so much fun playing!")

    elif choice == "3":
        energy = min(100, energy + 30)
        hunger = max(0, hunger - 10)
        print("😴", pet_name, "took a nice nap!")

    elif choice == "4":
        cleanliness = 100
        happiness = min(100, happiness + 5)
        print("🛁", pet_name, "is all clean now!")

    elif choice == "5":
        health = min(100, health + 20)
        happiness = max(0, happiness - 5)
        print("🏥", pet_name, "went to the vet and feels better!")

    elif choice == "6":
        print("👋 Thanks for playing with your pet!")
        break

    else:
        print("❌ Oops! That's not a valid choice.")
        continue

    # Time passes after every action
    hunger = max(0, hunger - 5)
    happiness = max(0, happiness - 3)
    energy = max(0, energy - 4)
    cleanliness = max(0, cleanliness - 2)

    if cleanliness < 20:
        happiness = max(0, happiness - 5)
        print("😖", pet_name, "is feeling dirty.")

    if hunger == 0:
        health = max(0, health - 10)
        print("🍽️", pet_name, "is starving!")

    if happiness == 0:
        health = max(0, health - 5)
        print("💔", pet_name, "is feeling really sad.")

    if energy == 0:
        print("😴", pet_name, "got too tired and fell asleep!")
        energy = 30

    if (hunger > 80 and happiness > 80 and energy > 80
            and health > 80 and cleanliness > 80):
        level += 1
        print("🎉⭐ Level Up! Your pet is now Level", level, "🎉")

    print("\n📊 ----- Pet Stats ----- 📊")
    print("⭐ Level:", level)
    print("🍖 Hunger:", hunger)
    print("😊 Happiness:", happiness)
    print("⚡ Energy:", energy)
    print("❤️ Health:", health)
    print("🛁 Cleanliness:", cleanliness)

if health == 0:
    print("\n💀 Game Over!")
    print("😢", pet_name, "couldn't survive.")






class Pet:
    def __init__(self, name, pet_type):
        self.name = name
        self.pet_type = pet_type
        self.hunger = 80
        self.happiness = 80
        self.energy = 80
        self.health = 100
        self.cleanliness = 80
        self.level = 1

    def show_stats(self):
        print("\n📊 ----- Pet Stats ----- 📊")
        print("📛 Name:", self.name)
        print("🐾 Type:", self.pet_type)
        print("⭐ Level:", self.level)
        print("🍖 Hunger:", self.hunger)
        print("😊 Happiness:", self.happiness)
        print("⚡ Energy:", self.energy)
        print("❤️ Health:", self.health)
        print("🛁 Cleanliness:", self.cleanliness)

    def feed(self):
        self.hunger = min(100, self.hunger + 20)
        self.health = min(100, self.health + 5)
        self.cleanliness = max(0, self.cleanliness - 10)
        print("🍖", self.name, "really liked the food!")

    def play(self):
        self.happiness = min(100, self.happiness + 20)
        self.hunger = max(0, self.hunger - 10)
        self.energy = max(0, self.energy - 15)
        self.cleanliness = max(0, self.cleanliness - 10)
        print("🎉", self.name, "had so much fun playing!")

    def sleep(self):
        self.energy = min(100, self.energy + 30)
        self.hunger = max(0, self.hunger - 10)
        print("😴", self.name, "took a nice nap!")

    def clean(self):
        self.cleanliness = 100
        self.happiness = min(100, self.happiness + 5)
        print("🛁", self.name, "is all clean now!")

    def visit_vet(self):
        self.health = min(100, self.health + 20)
        self.happiness = max(0, self.happiness - 5)
        print("🏥", self.name, "went to the vet and feels better!")

    def time_passes(self):
        self.hunger = max(0, self.hunger - 5)
        self.happiness = max(0, self.happiness - 3)
        self.energy = max(0, self.energy - 4)
        self.cleanliness = max(0, self.cleanliness - 2)

        if self.cleanliness < 20:
            self.happiness = max(0, self.happiness - 5)
            print("😖", self.name, "is feeling dirty.")

        if self.hunger == 0:
            self.health = max(0, self.health - 10)
            print("🍽️", self.name, "is starving!")

        if self.happiness == 0:
            self.health = max(0, self.health - 5)
            print("💔", self.name, "is feeling really sad.")

        if self.energy == 0:
            print("😴", self.name, "got too tired and fell asleep!")
            self.energy = 30

        if (self.hunger > 80 and self.happiness > 80 
            and self.energy > 80 and self.health > 80 
            and self.cleanliness > 80):
            self.level += 1
            print("🎉⭐ Level Up! Your pet is now Level", self.level)


# Main Program
print("🐾 **************************** 🐾")
print("  🐶🐱 Welcome to My Digital Pet! 🐉🐸")
print("🐾 **************************** 🐾")

pet_name = input("🐾 Enter your pet's name: ")
pet_type = input("🦴 Enter your pet's type: ")

pet = Pet(pet_name, pet_type)

print("\n🎉 Your pet is ready!")
pet.show_stats()


while pet.health > 0:
    print("\n====== 🐾 MENU 🐾 ======")
    print("1. 🍖 Feed")
    print("2. 🎾 Play")
    print("3. 😴 Sleep")
    print("4. 🛁 Clean")
    print("5. 🏥 Visit Vet")
    print("6. 🚪 Quit")

    choice = input("👉 Choose an option (1-6): ")

    if choice == "1":
        pet.feed()

    elif choice == "2":
        pet.play()

    elif choice == "3":
        pet.sleep()

    elif choice == "4":
        pet.clean()

    elif choice == "5":
        pet.visit_vet()

    elif choice == "6":
        print("👋 Thanks for playing with your pet!")
        break

    else:
        print("❌ Oops! That's not a valid choice.")
        continue

    pet.time_passes()
    pet.show_stats()


if pet.health == 0:
    print("\n💀 Game Over!")
    print("😢", pet.name, "couldn't survive.")