# Problem 10: Modify the tuple
# Given a nested tuple. Write a program to modify the first item (22) of a list inside the following tuple to 222
nested_tuple = ((11, [22, 33]), 44, 55)
nested_list = list(nested_tuple[0])
nested_list[0] = 222
modified_tuple = (tuple(nested_list),) + nested_tuple[1:]

print(modified_tuple)