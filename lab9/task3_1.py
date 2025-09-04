"""
Calculator module

Provides basic arithmetic functions:
- add(a, b): Returns the sum of a and b.
- subtract(a, b): Returns the difference of a and b.
- multiply(a, b): Returns the product of a and b.
- divide(a, b): Returns the quotient of a and b, handles division by zero.
"""

def add(a, b):
    """
    Return the sum of a and b.

    Args:
        a (float or int): First number.
        b (float or int): Second number.

    Returns:
        float or int: The sum of a and b.
    """
    return a + b

def subtract(a, b):
    """
    Return the difference of a and b (a - b).

    Args:
        a (float or int): First number.
        b (float or int): Second number.

    Returns:
        float or int: The difference of a and b.
    """
    return a - b

def multiply(a, b):
    """
    Return the product of a and b.

    Args:
        a (float or int): First number.
        b (float or int): Second number.

    Returns:
        float or int: The product of a and b.
    """
    return a * b

def divide(a, b):
    """
    Return the quotient of a and b (a / b).
    Returns an error message if b is zero.

    Args:
        a (float or int): Numerator.
        b (float or int): Denominator.

    Returns:
        float or str: The quotient of a and b, or error message if b is zero.
    """
    if b == 0:
        return "Error: Division by zero"
    return a / b

if __name__ == "__main__":
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))
    print(f"Add: {add(x, y)}")
    print(f"Subtract: {subtract(x, y)}")
    print(f"Multiply: {multiply(x, y)}")
    print(f"Divide: {divide(x, y)}")
    