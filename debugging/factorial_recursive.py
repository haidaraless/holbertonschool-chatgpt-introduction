#!/usr/bin/python3
import sys

def factorial(n):
    # Function Description:
    # This function computes the factorial of a non-negative integer using recursion.

    # Parameters:
    # n (int): A non-negative integer whose factorial is to be calculated.

    # Returns:
    # int: The factorial value of the input integer n.

    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Check if the correct number of command-line arguments is provided
if len(sys.argv) != 2:
    print("Usage: python3 factorial.py <non-negative integer>")
    sys.exit(1)

# Convert input to integer
n = int(sys.argv[1])

# Calculate factorial and print the result
f = factorial(n)
print(f)
