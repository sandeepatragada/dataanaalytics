# Using numpy (recommended for data analytics)
import numpy as np
random_numbers = np.random.randint(1, 101, size=100)  # Generates integers between 1 and 100

# Alternative using random module
import random
random_numbers_2 = [random.randint(1, 100) for _ in range(100)]

# If you want floating point numbers between 0 and 1
random_floats = np.random.random(100)

# Print the first few numbers to verify
print("First 5 random integers:", random_numbers[:5])
print("First 5 alternative random integers:", random_numbers_2[:5])
print("First 5 random floats:", random_floats[:5])