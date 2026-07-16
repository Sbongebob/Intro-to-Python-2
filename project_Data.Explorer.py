import matplotlib.pyplot as plt
import statistics

# FIFA World Cup data
countries = [
    "Brazil",
    "Germany",
    "Italy",
    "Argentina",
    "France",
    "Uruguay",
    "England",
    "Spain"
]

titles = [5, 4, 4, 3, 2, 2, 1, 1]

# Calculate the mean
average_titles = statistics.mean(titles)

# Print the results
print("FIFA World Cup Titles by Country")
print("--------------------------------")
print("Countries:", countries)
print("Titles:", titles)
print("Average Number of Titles:", average_titles)

# -------------------------
# PIE CHART
# -------------------------
plt.figure(figsize=(8, 6))

plt.pie(
    titles,
    labels=countries,
    autopct="%1.1f%%"
)

plt.title("FIFA World Cup Titles by Country (Pie Chart)")

plt.show()

# -------------------------
# LINE GRAPH
# -------------------------
plt.figure(figsize=(8, 6))

plt.plot(countries, titles, marker='o')

plt.title("FIFA World Cup Titles by Country (Line Graph)")
plt.xlabel("Country")
plt.ylabel("Number of World Cup Titles")

plt.xticks(rotation=45)

plt.show()