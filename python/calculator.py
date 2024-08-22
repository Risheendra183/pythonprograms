import os

# Calculation functions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y

# Dictionary mapping operators to functions
operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

def calculator():
    while True:
        num1 = float(input("Enter number 1: "))
        print("Available operations:", ', '.join(operations.keys()))

        operator = input("Enter the operation: ")
        if operator not in operations:
            print("Invalid operator. Please try again.")
            continue

        num2 = float(input("Enter number 2: "))

        calc_function = operations[operator]
        output = calc_function(num1, num2)
        print(f"{num1} {operator} {num2} = {output}")

        should_continue = input(f"Enter 'y' to continue with {output}, 'n' to start a new calculation, or any other key to exit: ").lower()
        if should_continue == 'n':
            print("Goodbye!")
            break

        elif should_continue != 'y':
            print("Invalid input. Goodbye!")
            break

if __name__ == "__main__":
    # Clear the console by printing empty lines
    os.system('cls' if os.name == 'nt' else 'clear')
    calculator()
