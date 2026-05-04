numbers = [1, 4, 5, 6, 7]
n = 7
missing = list(set(range(1, n + 1)) - set(numbers))
print("Missing numbers:",missing)
