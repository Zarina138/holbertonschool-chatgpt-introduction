#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a given non-negative integer using recursion.

    Parameters:
        n (int): The number for which the factorial is to be computed.
                 Must be a non-negative integer.

    Returns:
        int: The factorial of the given number 'n'.
             If n == 0, returns 1 (by definition of factorial).
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Get the number from command-line arguments, compute its factorial, and print it
f = factorial(int(sys.argv[1]))
print(f)
