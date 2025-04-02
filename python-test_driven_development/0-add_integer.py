#!/usr/bin/python3
"""
This module contains a function that adds two integers.
The function accepts two parameters and returns their sum.
"""


def add_integer(a, b=98):
    """
    Adds two integers and returns the result.
    Args:
        a: first number (integer or float)
        b: second number (integer or float), defaults to 98
    Returns:
        The addition of a and b as an integer
    Raises:
        TypeError: If a or b is not an integer or float
    """
    # Check if a is an integer or float
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    
    # Check if b is an integer or float
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    
    # Cast float numbers to integers
    a = int(a)
    b = int(b)
    
    return a + b
