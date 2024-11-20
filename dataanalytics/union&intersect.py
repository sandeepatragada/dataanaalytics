# Function to calculate union of two sets
def union_of_sets(set1, set2):
    return set1.union(set2)

# Function to calculate intersection of two sets
def intersection_of_sets(set1, set2):
    return set1.intersection(set2)

# Input: Two sets from the user
set1 = set(map(int, input("Enter elements of the first set (space separated): ").split()))
set2 = set(map(int, input("Enter elements of the second set (space separated): ").split()))

# Calculate union and intersection
union = union_of_sets(set1, set2)
intersection = intersection_of_sets(set1, set2)

# Display the results
print(f"Union of the sets: {union}")
print(f"Intersection of the sets: {intersection}")
