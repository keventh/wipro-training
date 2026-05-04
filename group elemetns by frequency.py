from collections import Counter, defaultdict
list = {1, 2, 2, 3, 3, 3, 4, 4}
freq = Counter(list)
grouped = defaultdict(list)
for num,count in freq.items():
    grouped[count].append(num)
print(dict(grouped))