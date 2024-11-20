import math

# Function to calculate factorial manually
def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)

# Function to calculate combinations manually
def calculate_combinations(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))

# Input: Total items (n) and items to select (r)
n = int(input("Enter the total number of items (n): "))
r = int(input("Enter the number of items to select (r): "))

# Calculate combinations
combinations = calculate_combinations(n, r)

# Display the result
print(f"The number of combinations (C({n}, {r})) is: {combinations}")
