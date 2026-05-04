#In tuples you can't modify-They are immutable
numbers = (10, 20, 30 ,40)
numbers[1] = 99 #This can't be done in tuples


#if i want to iterate from the last index
for num in reversed(numbers):
    print(num)  