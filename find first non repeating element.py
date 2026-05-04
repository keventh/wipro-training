from collections import Counter
list = [4, 5, 1, 2, 0, 5, 1, 2]
freq = Counter(list)
for num in list:
    if freq[num] == 1:
        print(num)
        break