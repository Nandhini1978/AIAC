def centimeters_to_inches(cm):
    return cm / 2.54

cm_value = float(input("Enter value in centimeters: "))
inches = centimeters_to_inches(cm_value)
print(f"{cm_value} centimeters converts to {inches:.5f} inches")