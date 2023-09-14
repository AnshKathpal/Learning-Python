numbers = []

for x in range(1,11):
    numbers.append(x)
print(numbers)

#append is used to add the elements in the list
numbers.append(11)
print(numbers)

#remove is used to remove an element in the list
numbers.remove(11)
print(numbers)

#getting the element on the index 3
print(numbers[3])

#modifying the element
numbers[9] = 11
print(numbers)

#getting the length of the list
print(len(numbers))

#sorting
numbers.sort(reverse=True)
print(numbers)