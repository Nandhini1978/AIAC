def sum_even_odd(numbers):
    """
    Calculates the sum of even and odd numbers in a given list.
    Args:
        numbers (list of int): List of integers to process.
    Returns:
        tuple: A tuple containing two integers:
            - Sum of even numbers.
            - Sum of odd numbers.
    """
    # Calculate sum of even numbers using list comprehension
    even_sum = sum(n for n in numbers if n % 2 == 0)
    # Calculate sum of odd numbers using list comprehension
    odd_sum = sum(n for n in numbers if n % 2 != 0)
    # Return both sums as a tuple
    return even_sum, odd_sum

if __name__ == "__main__":
    # Example list of numbers
    nums = [1, 2, 3, 4, 5, 6]
    # Call the function and unpack the results
    even, odd = sum_even_odd(nums)
    # Display the sum of even numbers
    print(f"Sum of even numbers: {even}")
    # Display the sum of odd numbers
    print(f"Sum of odd numbers: {odd}")