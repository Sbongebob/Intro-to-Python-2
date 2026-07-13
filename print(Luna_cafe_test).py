menu = [
    "Croissant",
    "Latte",
    "Black coffee",
    "Espresso",
    "Muffins",
    "Avocado toast",
    "Matcha",
    "Cappuccino"
]

prices = {
    "croissant": 3.50,
    "latte": 5.00,
    "black coffee": 3.00,
    "espresso": 3.00,
    "muffins": 3.50,
    "avocado toast": 8.50,
    "matcha": 5.50,
    "cappuccino": 5.00,
    # Daily specials
    "cake pop": 2.50,
    "iced tea": 4.00,
    "lemonade": 4.00,
    "lemon iced toast": 7.50,
    "hot chocolate": 4.50,
}

print("Welcome to Python Café!")
print("First take a look at the menu please!\n")

day = 1

def specials(day):
    print("Today's Daily Special:")
    if day == 1:
        print("- Cake pop: $2.50")
    elif day == 2:
        print("- Iced tea: $4.00")
    elif day == 3:
        print("- Lemonade: $4.00")
    elif day == 4:
        print("- Lemon iced toast: $7.50")
    else:
        print("- Hot chocolate: $4.50")

# Reset the day if needed
if day > 5:
    day = 1

# Show today's special
specials(day)

# Show the regular menu
print("\nRegular Menu:")
for item in menu:
    print(f"- {item}: ${prices[item.lower()]:.2f}")

# Function to find the price
def get_price(item):
    return prices.get(item.lower())

# Customer ordering
total = 0

while True:
    order = input("\nWhat would you like to order? (Type 'done' to finish): ").strip()

    if order.lower() == "done":
        break

    price = get_price(order)

    if price is not None:
        print(f"{order.title()} costs ${price:.2f}")
        total += price
    else:
        print("Sorry, that item is not on the menu.")

print("\n------------------------")
print(f"Your total is: ${total:.2f}")
print("Thank you for visiting Python Café!")

# Move to the next day
day += 1

