
def classify_age_nested(age):
    if age >= 0:
        if age <= 12:
            return "Child"
        elif age <= 19:
            return "Teenager"
        elif age <= 35:
            return "Young Adult"
        elif age <= 59:
            return "Adult"
        else:
            return "Senior Citizen"
    else:
        return "Invalid Age"

def classify_age_direct(age):
    if age < 0:
        return "Invalid Age"
    elif age <= 12:
        return "Child"
    elif age <= 19:
        return "Teenager"
    elif age <= 35:
        return "Young Adult"
    elif age <= 59:
        return "Adult"
    else:
        return "Senior Citizen"


age = int(input("Enter your age: "))

# Call both functions
result_nested = classify_age_nested(age)
result_direct = classify_age_direct(age)

# Print results
print("\n--- Age Classification Results ---")
print("Using Nested if-elif-else:", result_nested)
print("Using Direct if-elif-else:", result_direct)

