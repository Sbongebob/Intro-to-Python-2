# Python Café Menu

# Stores menu items and prices
prices = {
    "croissant": 3.50,
    "latte": 5.00,
    "black coffee": 3.00,
    "espresso": 3.00,
    "muffins": 3.50,
    "avocado toast": 8.50,
    "matcha": 5.50,
    "cappuccino": 5.00,
}

# Function to find the price of an item
def get_price(item):
    return prices.get(item.lower().strip())

print("Welcome to Python Café!")
print("\nMenu:")
for item, price in prices.items():
    print(f"- {item.title()}: ${price:.2f}")

print()

# Customer ordering
total = 0

while True:
    order = input("What would you like to order? (Type 'done' to finish): ").strip()

    if order.lower() == "done":
        break

    price = get_price(order)

    if price is not None:
        print(f"{order.title()} costs ${price:.2f}")
        total += price
    else:
        print("Sorry, that item is not on the menu.")

print("\n-------------------")
print(f"Your total is: ${total:.2f}")
print("Thank you for visiting Python Café!")