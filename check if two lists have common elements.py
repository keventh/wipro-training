list1 = [1, 2, 3, 4]
list2 = [5, 6, 3, 8]
if set(list1) & set(list2):
    print("Common element exists")
else:
    print("Common element does not exist")