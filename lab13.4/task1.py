"""Compute and print the squares of a list of numbers.

This script demonstrates a Pythonic list comprehension replacing a manual loop.
"""

numbers = [1, 2, 3, 4, 5]
squares = [n ** 2 for n in numbers]
print(squares)