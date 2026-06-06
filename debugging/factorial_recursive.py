#!/usr/bin/python3
import sys

def factorial(n):
    """
    Function Description:
    Calculates the factorial of a given positive integer recursively.
    
    Parameters:
    n (int): The integer number for which the factorial is to be calculated.
    
    Returns:
    int: The calculated factorial of the given number. Returns 1 if n is 0.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

if __name__ == "__main__":
    f = factorial(int(sys.argv[1]))
    print(f)
