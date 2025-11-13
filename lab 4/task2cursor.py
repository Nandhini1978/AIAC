def cm_to_inches(cm):
    return cm / 2.54

try:
    cm_input = float(input("Enter value in centimeters: "))
    inches = cm_to_inches(cm_input)
    print(f"{cm_input} centimeters converts to {inches:.5f} inches")
except ValueError:
    print("Invalid input. Please enter a numeric value.")
