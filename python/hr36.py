# Function to find the maximum length of a substring that can be converted with maxCost
def max_length_substring(str1, str2, maxCost):
    n = len(str1)
    left = 0
    max_length = 0
    current_cost = 0

    for right in range(n):
        # Calculate the cost of transforming str1[right] to str2[right]
        cost = abs(ord(str1[right]) - ord(str2[right]))
        
        # Add the cost to the current cost
        current_cost += cost

        # If the current cost exceeds maxCost, move the left pointer
        while current_cost > maxCost:
            current_cost -= abs(ord(str1[left]) - ord(str2[left]))
            left += 1

        # Update the maximum length
        max_length = max(max_length, right - left + 1)

    return max_length

# Read the number of test cases
t = int(input().strip())

# Process each test case
for _ in range(t):
    # Read the input for each test case
    str1 = input().strip()
    str2 = input().strip()
    maxCost = int(input().strip())

    # Calculate and print the maximum length of a convertible substring
    result = max_length_substring(str1, str2, maxCost)
    print(result)
