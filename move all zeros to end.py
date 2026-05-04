numbers = [1, 0, 3, 0, 5]
non_zero = [x for x in numbers if x != 0]
zeros = [0] * numbers.count(0)
result = non_zero + zeros
print(result)