file_path = r'c:\Users\DELL\OneDrive\a.txt'

with open(file_path, 'r', encoding='utf-8') as file:
    lines = file.readlines()
    print(f'Number of lines: {len(lines)}')