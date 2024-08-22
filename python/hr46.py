# Function to calculate the yield for a given arrangement of Barley and Maize plants
def calculate_yield(m, n, barley, maize):
    total_yield = 0

    # Calculate yield for Barley plants
    total_yield += barley * 120

    # Calculate yield for Maize plants
    total_yield += maize * (40 + 20 * (maize - 1))

    return total_yield

# Read the number of test cases
T = int(input().strip())

# Iterate through each test case
for _ in range(T):
    # Read input for each test case
    m, n, barley, maize = map(int, input().split())

    # Calculate the maximum yield for the current test case
    max_yield = calculate_yield(m, n, barley, maize)

    # Print the maximum yield for the current test case
    print(max_yield)
