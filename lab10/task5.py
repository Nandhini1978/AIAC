def divide_numbers(numerator, denominator):
    try:
        return numerator / denominator
    except ZeroDivisionError:
        print("Error: denominator cannot be zero.")
        return None
    except TypeError:
        print("Error: both inputs must be numbers.")
        return None

print(divide_numbers(10, 0))