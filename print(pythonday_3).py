print(5 + 3)
print(4 * 3)
print(10 / 2)
print(4 ** 2)
print(9 // 4)

a = 10
b = 3
print(a // b) # integer division
print(a % b) # modulus
print(a ** b) # exponentiation

print(5 == 5) 
print(3 != 4)
print(7 > 3)
print(2 < 5)
print(6 >= 6)
print(4 <= 10)
print(7 >= 5)

print(not True)  

# USER INPUT

print("=== Carbon Footprint Calculator (grams) ===")

bus_trips = int(input("Bus trips: "))
computer_hours = float(input("Hours on computer: "))
electric_car_miles = float(input("Electric car miles: "))
gas_car_miles = float(input("Gas car miles: "))
hybrid_car_miles = float(input("Hybrid car miles: "))

light_hours = float(input("Hours lights on per day: "))
num_lights = int(input("Number of lights: "))

light_rail_trips = int(input("Light rail trips: "))
showers = int(input("Showers: "))
meals = int(input("Meals cooked: "))

stove = input("Stove type (electric/induction/gas): ").lower()

ac_hours = float(input("AC hours per day: "))

ferry_walk = int(input("Ferry (walk) trips: "))
ferry_car = int(input("Ferry (car) trips: "))

plane_trips = int(input("Plane trips per year: "))

# CALCULATIONS (ALL grams)

total = 0

# Bus: 1.6 lbs → 726 g
total += bus_trips * 726

# Computer: 60 g per hour
total += computer_hours * 60

# Electric car: 140 g per mile
total += electric_car_miles * 140

# Gas car: 0.4 kg → 400 g per mile
total += gas_car_miles * 400

# Hybrid car: 250 g per mile
total += hybrid_car_miles * 250

# Lights: 0.045 lbs → 20 g per hour per light
total += light_hours * num_lights * 20

# Light rail: 3 lbs → 1361 g per trip
total += light_rail_trips * 1361

# Shower: 1.2 kg → 1200 g each
total += showers * 1200

# Meals (stove types)
if stove == "electric":
    total += meals * 300
elif stove == "induction":
    total += meals * 180
else:  # gas
    total += meals * 450

# AC: 2.5 lbs → 1134 g per hour
total += ac_hours * 1134

# Ferry walk: 14 oz → 397 g per trip
total += ferry_walk * 397

# Ferry car: 3.735 oz → 106 g per trip
total += ferry_car * 106

# Plane: 25 tons → 25,000,000 g per trip
total += plane_trips * 25_000_000

# REPORT

print("\n=== REPORT ===")
print(f"Total CO2 emissions: {total:.0f} grams")

if total < 500_000:
    print("Low impact 🌱")
elif total < 2_000_000:
    print("Medium impact 🌿")
else:
    print("High impact 🔥")