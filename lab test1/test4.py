import csv

filename = r'c:\Users\DELL\OneDrive\labtest1.csv'

with open(filename, 'r') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=' ')
    for row in reader:
        # Remove empty keys caused by extra spaces
        row = {k: v for k, v in row.items() if k}
        name = row['Name']
        marks = [int(row['sub1']), int(row['sub2']), int(row['sub3'])]
        total = sum(marks)
        average = total / 3
        print(f"Student: {name}, Total: {total}, Average: {average:.2f}")
