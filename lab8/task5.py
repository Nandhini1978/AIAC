def convert_date_format(date_str):
    """
    Converts a date from 'YYYY-MM-DD' to 'DD-MM-YYYY' format.
    Example: '2023-10-15' -> '15-10-2023'
    """
    parts = date_str.split('-')
    if len(parts) != 3:
        raise ValueError("Invalid date format. Expected 'YYYY-MM-DD'.")
    yyyy, mm, dd = parts
    return f"{dd}-{mm}-{yyyy}"

# Example usage
if __name__ == "__main__":
    print(convert_date_format("2023-10-15"))  # Output: 15-10-2023