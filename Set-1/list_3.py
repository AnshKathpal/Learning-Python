3. #Write a Python program to create a list of numbers from 1 to 10, and then add a number, remove a number, and sort the list.
    #- *Input*: None
    #- *Output*: "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20]..."


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