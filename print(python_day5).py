# define the function
def say_hello(name):
    print(f"Hello, {name}!")

#call the function with different name 
say_hello("Emma")
say_hello("Liam")
say_hello("Sophia")

def introduce(first_name, last_name, age):
    print("Let's meet our student!")
    print(first_name, "is", age, "years old")

    print(first_name, last_name, sep="-")
    print(first_name, "is", age, "years old.", sep="")

    print("Name:", first_name, end=" ")
    print(last_name)

    print(first_name * 2, last_name * 3)

    print("*" * 20)

# Call the function with your own values!
introduce("Niki", "Smith", 16)

def place_steps():
    for step in range(5):
        print("Place STEP")
    print("Stair complete!")

def place_steps2(step):
    for i in range(step):
        print("Place STEP")
    print("Stair complete!")

if __name__ == "__main__":
    step_amount = int(input("How many steps do you want? "))
    place_steps2(step_amount)

def place_torches(amount):
    for i in range(amount):
        if i % 5 == 0:
            print("Placing torch at position", i, "- This glowstone is rather bright")
        else:
            print("Placing torch at position", i)


def build_guard_tower():
    for floor in range(1, 4):  # 3 floors
        for block in range(1, 5):  # 4 blocks per floor
            print("Floor", floor, "Block", block)

            if block % 2 == 0:
                print("Place TORCH")


def collect_logs():
    logs = 0

    while logs < 64:
        logs += 1
        print("Chop log", logs)

        if logs == 60:
            print("Inventory nearly full!")


# Run the functions
build_guard_tower()
collect_logs()

def build_reinforced_wall():
    for block in range(1, 21):  # 20 wall blocks
        if block % 4 == 0:
            block_type = "COBBLESTONE"
        else:
            block_type = "PLANK"

        print(block_type, "at position", block)

        if block % 5 == 0:
            print("Defense checkpoint reached!")


def night_patrol():
    energy = 100
    minute = 0

    while minute < 10 and energy > 0:
        minute += 1

        print("Patrolling...")

        energy -= 12
        print("Current energy:", energy)

        if minute % 3 == 0:
            print("Scanning area for mobs...")

        if energy < 30:
            print("Warning: Low power!")

        if energy <= 0:
            print("Shutdown...")
            break


# Run the functions
build_reinforced_wall()
night_patrol()