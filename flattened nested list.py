nested = [1, [2, 3], [4, [5, 6]], 7]
flat =[]
for item in nested:
    if isinstance(item,list):
        for sub in item:
            flat.append(sub)
    else:
        flat.append(item)
print(flat)