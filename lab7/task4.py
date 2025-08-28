def compute_ratios(values):
    results = []
    for i in range(len(values) - 1):
        for j in range(i, len(values)):
            try:
                ratio = values[i] / (values[j] - values[i])
                results.append(ratio)
            except ZeroDivisionError:
                # Skip this calculation if division by zero occurs
                continue
    return results

nums = [5, 10, 15, 20, 25]
print(compute_ratios(nums))