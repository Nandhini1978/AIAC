def calculate_average(scores):
    if not scores:
        raise ValueError("scores cannot be empty")
    return sum(scores) / len(scores)

def find_highest(scores):
    if not scores:
        raise ValueError("scores cannot be empty")
    highest = scores[0]
    for s in scores[1:]:
        if s > highest:
            highest = s
    return highest

def find_lowest(scores):
    if not scores:
        raise ValueError("scores cannot be empty")
    lowest = scores[0]
    for s in scores[1:]:
        if s < lowest:
            lowest = s
    return lowest

def process_scores(scores):
    avg = calculate_average(scores)
    highest = find_highest(scores)
    lowest = find_lowest(scores)

    print("Average:", avg)
    print("Highest:", highest)
    print("Lowest:", lowest)
    return avg, highest, lowest

process_scores([85, 90, 78, 92, 88])
process_scores([70, 75, 80, 65, 90])