# Price Manager
# Stores menu items and prices using a dictionary

prices = {
    "Croissant": 3.50,
    "Latte": 5.00,
    "Black coffee": 3.00,
    "Espresso": 3.00,
    "Muffins": 3.50,
    "Avocado toast": 8.50,
    "Matcha": 5.50,
    "Cappuccino": 5.00,
}

# Function to find the price of an item
def get_price(item):
    if item in prices:
        return prices[item]
    else:
        return None