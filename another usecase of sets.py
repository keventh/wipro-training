set1 = {1, 2, 3}
set2 = {3, 4, 5}

result = set1.union(set2)
print(result)

result = set1.difference(set2)
print(result)

result = set1.intersection(set2)
print(result)

#converting list into a set
numbers = [1,2,2,3,4,4,5]
unique_numbers = set(numbers)
print(unique_numbers)
