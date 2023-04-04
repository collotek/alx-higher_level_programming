#!/usr/bin/python3
"""A function that adds two numbers"""

def add_integer(a, b=98):
    """Return the result of adding a and b
    a and b are first casted into integers if float before addition
    Raises:
        TypeError: If a or b are neither floats or integers
    """
    if (isinstance(a, int) == False and isinstance(a, float) == False):
        raise TypeError("a must be an integer")
    if (isinstance(b, int) == False and isinstance(b, float) == False):
            raise TypeError("b must be an integer")
    return int(a) + int (b)
print(add_integer('string', 2))
       
    
