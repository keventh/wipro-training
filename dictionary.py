student = {
    "name" : "Rahul",
    "age" : 21,
    "course" : "Python",
}

print(student)
print(student["name"])
print(student["course"])

#add a new key value pair
student["city"] = "Hyderabad"
print(student)

#update the data
student["age"] = 25
print(student)

#delete
del student["city"]
print(student)

#keys iteration
for key in student:
    print(key)

#value iteration
for value in student.values():
    print(value)

#loop through key-value pairs
for key, value in student.items():
    print(key, value)