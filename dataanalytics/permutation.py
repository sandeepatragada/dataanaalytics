import itertools

# Function to generate permutations
def generate_permutations(elements, r):
    return list(itertools.permutations(elements, r))

# Input: List of elements and number of selections (r)
elements = input("Enter elements separated by space: ").split()
r = int(input("Enter the number of elements to select (r): "))

# Generate permutations
permutations = generate_permutations(elements, r)

# Display the result
print(f"All permutations of {r} elements from the given set are:")
for perm in permutations:
    print(perm)
