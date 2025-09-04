def assign_grade(score):
    """
    Assigns a grade based on the score:
    90-100: A
    80-89: B
    70-79: C
    60-69: D
    <60: F
    Handles invalid inputs (non-numeric or out of range).
    """
    if not isinstance(score, (int, float)):
        return "Invalid input"
    if score < 0 or score > 100:
        return "Invalid input"
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
# Test cases
if __name__ == "__main__":
    test_scores = [100, 90, 89, 80, 79, 70, 69, 60, 59, 0, -5, 105, "eighty"]
    for score in test_scores:
        print(f"Score: {score} => Grade: {assign_grade(score)}")