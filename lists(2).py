numbers = [10, 20, 30, 40, 50]

#insert
numbers.insert(1, 100)
print(numbers)
#remove
numbers.remove(30)
print(numbers)

#remove last number
numbers.pop()
print(numbers)

#slicing
numbers = [10, 20, 30, 40, 50]
print(numbers[1:4])

#iterate though list
for num in numbers:
    print(num)

#length of the list
print(len(numbers))