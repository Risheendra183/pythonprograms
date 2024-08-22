import math

# Function to calculate the score for a given ball number
def calculate_score(ball_number):
    # Count the number of factors for the ball number
    factors_count = 0
    for i in range(1, int(math.sqrt(ball_number)) + 1):
        if ball_number % i == 0:
            factors_count += 1
            # If i and ball_number/i are different, count both factors
            if i != ball_number // i:
                factors_count += 1

    return factors_count

# Function to determine the winner of the game for a given test case
def determine_winner(starting_player, N):
    mahesh_score = 0
    pranay_score = 0

    for ball_number in range(1, N + 1):
        # Calculate the score for the current ball number
        score = calculate_score(ball_number)

        # Update the respective player's score based on the starting player
        if starting_player == "Mahesh":
            if ball_number % 2 == 1:
                mahesh_score += score
            else:
                pranay_score += score
        else:
            if ball_number % 2 == 1:
                pranay_score += score
            else:
                mahesh_score += score

    # Determine the winner or if it's a tie
    if mahesh_score % 2 == 1 and pranay_score % 2 == 0:
        return "Mahesh"
    elif mahesh_score % 2 == 0 and pranay_score % 2 == 1:
        return "Pranay"
    else:
        return "tie"

# Read the number of test cases
t = int(input().strip())

# Iterate through each test case
for _ in range(t):
    # Read input for each test case
    name, N = input().split()
    N = int(N)

    # Determine the winner and print the result
    winner = determine_winner(name, N)
    print(winner)
