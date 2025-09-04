def calculator(a,d,operation):
    if operation == "add":
        return a + d
    elif operation == "subtract":
        return a - d
    elif operation == "multiply":
        return a * d
    elif operation == "divide":
        if d != 0:
            return a / d
        else:
            return "Error: Division by zero"
    else:
        return "Error: Invalid operation"
if __name__ == "__main__":
    print(calculator(10, 5, "add"))        # Output: 15
    print(calculator(10, 5, "subtract"))   # Output: 5
    print(calculator(10, 5, "multiply"))   # Output: 50
    print(calculator(10, 5, "divide"))     # Output: 2.0
    print(calculator(10, 0, "divide"))     # Output: Error: Division by zero
    print(calculator(10, 5, "modulus"))    # Output: Error: Invalid operation