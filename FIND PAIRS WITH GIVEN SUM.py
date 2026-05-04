def find_pairs(arr, target_sum):
    seen = set()
    pairs = []

    for num in arr:
        complement = target - num
        if complement in seen:
            pairs.append((complement, num))
        seen.add(num)
    return pairs
numbers = [2, 3, 4, 5, 6, 7, 8, 9]
target_sum = 7
result = find_pairs(numbers, target_sum)
print("Pairs with sum", target_sum, "are:")
for pair in result:
    print(pair)