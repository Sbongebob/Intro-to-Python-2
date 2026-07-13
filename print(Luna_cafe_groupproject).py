# Price Manager
# Stores menu items and prices using a dictionary

prices = {
    "Croissant": 3.50,
    "Latte": 5.00,
    "Black Coffee": 3.00,
    "Espresso": 3.00,
    "Muffins": 3.50,
    "Avocado Toast": 8.50,
    "Matcha": 5.50,
    "Cappuccino": 5.00,
}

# Function to find the price of an item
def get_price(item):
    if item in prices:
        return prices[item]
    else:
        return None


# Customer ordering
total = 0

while True:
    order = input("What would you like to order? (type done to finish): ").title()

    if order == "Done":
        break

    price = get_price(order)

    if price is not None:
        print(order, "costs $", price)
        total += price
    else:
        print("Sorry, that item is not on the menu.")

print("-------------------")
print("Your total is: $", total)
print("Thank you for visiting Python Café!")

