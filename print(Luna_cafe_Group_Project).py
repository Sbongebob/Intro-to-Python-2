menu = ["Croissant", "Latte", "Black coffee", "Espresso", "Muffins", "Avocado toast", "Matcha", "Cappuccino"]
playing = True
day = 1




while playing:
   print("Welcome to Python cafe!")
   print("First take a look at the menu please!")




   if day > 5:
       day = 1




   def specials(day):
       print("Todays daily special:")
   if day == 1:
       print("Cake pop : $2.50")
   elif day == 2:
       print("Iced tea : $4.00")
   elif day == 3:
       print("Lemonade : $4.00")
   elif day == 4:
       print("Lemon iced toast : $7.50")
   else:
       print("Hot chocolate : $4.50")


   specials(day)


   drinks=("latte", "black coffee", "matcha", "espresso", "cappuccino")
   food=("muffin", "avocado toast", "croissant")
   hot_drinks =("latte", "black coffee", "matcha", "espresso", "cappuccino",)
   cold_drinks =("matcha")
   latte = (5.00, "calories: 150")
   blackcoffee= (3.00, "calories: 5")
   matcha= (5.50, "calories: 100")
   espreso = (3.00, "calories: 5")
   cappuccino = (5.00, "calories: 75")
   muffin = (3.50, "calories: 400")
   avocadotoast = (8.50, "calories: 250")
   croissant = (3.50, "calories: 250")


   print(menu)
   print("Drinks: ", drinks)
   print("Food: ", food)




   prices = {
   "Croissant": 3.50,
   "Latte": 5.00,
   "Black Coffee": 3.00,
   "Espresso": 3.00,
   "Muffins": 3.50,
   "Avocado Toast": 8.50,
   "Matcha": 5.50,
   "Cappuccino": 5.00,
   "Cake Pop": 2.50,
   "Iced Tea": 4.00,
   "Lemonade": 4.00,
   "Lemon Iced Toast": 7.50,
   "Hot Chocolate": 4.50,
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
   print("")
   quit = input("Would you like to quit?(y/n): ").upper()
   if quit == "Y" or quit == "YES":
       break


   day += 1
