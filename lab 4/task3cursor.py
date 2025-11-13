def format_name(full_name):
    parts = full_name.strip().split()
    if len(parts) < 2:
        return full_name  # Return as is if not enough parts
    first = parts[0]
    last = " ".join(parts[1:])
    return f"{last} {first}"

user_input = input("Enter full name (First Last): ")
formatted = format_name(user_input)
print(f"Formatted name: {formatted}")
