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
