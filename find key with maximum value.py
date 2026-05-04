a = {'x': 1, 'y': 2, 'z': 3}
max_key = max(a, key=a.get)
print(max_key)