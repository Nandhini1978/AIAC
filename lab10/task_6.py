
def grade_elif(score):
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
print("--- Using elif ---")
print(grade_elif(95))
print(grade_elif(85))
print(grade_elif(75))
print(grade_elif(65))
print(grade_elif(55))