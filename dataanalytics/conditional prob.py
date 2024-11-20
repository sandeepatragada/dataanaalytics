# Function to calculate conditional probability P(A|B)
def conditional_probability(p_A_and_B, p_B):
    # Check if P(B) is not zero to avoid division by zero error
    if p_B == 0:
        return "Error: P(B) cannot be zero (division by zero is undefined)."
    
    # Calculate conditional probability P(A|B)
    return p_A_and_B / p_B

# Input: The user enters probabilities
p_A_and_B = float(input("Enter the probability of both A and B occurring (P(A ∩ B)): "))
p_B = float(input("Enter the probability of event B occurring (P(B)): "))

# Calculate conditional probability
p_A_given_B = conditional_probability(p_A_and_B, p_B)

# Output the result
print(f"The conditional probability P(A|B) is: {p_A_given_B}")
