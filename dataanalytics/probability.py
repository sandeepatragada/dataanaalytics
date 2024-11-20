def calculate_probability(favorable_outcomes, total_outcomes):
    # Ensure that the total outcomes is not zero to avoid division by zero error
    if total_outcomes == 0:
        return "Total outcomes cannot be zero."
    
    # Calculate probability
    probability = favorable_outcomes / total_outcomes
    return probability

# Input: Number of favorable outcomes and total outcomes
favorable_outcomes = int(input("Enter the number of favorable outcomes: "))
total_outcomes = int(input("Enter the total number of outcomes: "))

# Calculate probability
probability = calculate_probability(favorable_outcomes, total_outcomes)

# Display the result
print(f"The probability of the event is: {probability}")
