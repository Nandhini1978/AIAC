def find_common(a, b):
    b_set = set(b)
    res = []
    for x in a:
        if x in b_set and x not in res:
            res.append(x)
    return res

print(find_common([1, 2, 3], [2, 3, 4]))
print(find_common(['apple', 'banana'], ['banana', 'cherry']))