import random

# Player inventory (List)
inventory = []

# Player stats
health = 100
treasure = False

# World (Dictionary)
locations = {
    "forest": {
        "description": "Tall trees surround you. You hear birds singing.",
        "item": "Sword"
    },
    "river": {
        "description": "A rushing river blocks your path.",
        "item": "Boat"
    },
    "village": {
        "description": "A friendly village with a small shop.",
        "item": "Potion"
    },
    "cave": {
        "description": "A dark cave where a dragon sleeps."
    }
}

print("===================================")
print("     THE LOST TREASURE")
print("===================================")
print("Find the treasure before your health reaches 0!")
print()

while health > 0 and not treasure:

    print("\nHealth:", health)
    print("Inventory:", inventory)
    print("\nWhere would you like to go?")
    print("Forest | River | Village | Cave | Quit")

    choice = input("> ").lower().strip()

    if choice == "forest":
        print("\n" + locations["forest"]["description"])

        if "Sword" not in inventory:
            print("You found a Sword!")
            inventory.append("Sword")
        else:
            print("You already collected the Sword.")

    elif choice == "river":
        print("\n" + locations["river"]["description"])

        if "Boat" not in inventory:
            print("You found a Boat!")
            inventory.append("Boat")
        else:
            print("You enjoy the peaceful river.")

    elif choice == "village":
        print("\n" + locations["village"]["description"])

        if "Potion" not in inventory:
            print("You found a Health Potion!")
            inventory.append("Potion")
        else:
            print("The villagers welcome you back.")

        if "Potion" in inventory:
            use = input("Use the Potion? (yes/no): ").lower().strip()

            if use == "yes":
                health = min(100, health + 30)
                inventory.remove("Potion")
                print("Your health is now", health)

    elif choice == "cave":
        print("\n" + locations["cave"]["description"])

        if "Sword" in inventory:
            print("A dragon attacks!")

            if random.randint(1, 2) == 1:
                print("You defeated the dragon!")
                print("You found the Lost Treasure!")
                treasure = True
            else:
                print("The dragon burned you!")
                health -= 30

        else:
            print("You have no Sword!")
            print("The dragon attacks!")
            health -= 40

    elif choice == "quit":
        print("Thanks for playing!")
        break

    else:
        print("That isn't a valid choice.")
        health -= 10

# Ending
if treasure:
    print("\n🏆 Congratulations! You found the Lost Treasure!")
elif health <= 0:
    print("\n💀 You ran out of health. Game Over.")