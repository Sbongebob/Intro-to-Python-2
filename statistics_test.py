#Median formula
import statistics
data = {10, 5, 8, 12, 3}
median_value = statistics.median(data)
print("Median:", median_value)

#A mode
import statistics
data = [4, 2, 4, 3, 2, 4, 5]
mode_value = statistics.mode(data)
print("Mode:", mode_value)


# Plant heights (in inches)
heights = [9, 11, 9, 13, 8]

# Mean
mean = sum(heights) / len(heights)

# Median
sorted_heights = sorted(heights)
middle = len(sorted_heights) // 2
median = sorted_heights[middle]

# Mode
counts = {}

for height in heights:
    if height in counts:
        counts[height] += 1
    else:
        counts[height] = 1

mode = max(counts, key=counts.get)

# Display results
print("Plant Heights:", heights)
print("Mean:", mean)
print("Median:", median)
print("Mode:", mode)


#class fav subjects data
import statistics
import numpy as np
import matplotlib.pyplot as plt 
class_data = {
              "math": 16,
              "science": 8,
              "english": 3,
              "history": 1,
              "economics": 1,
              "music_theory": 2}

mode_class = statistics.mode(class_data)

print(mode_class)

