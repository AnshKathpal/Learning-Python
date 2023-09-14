#6. Write a Python program that counts the number of vowels in a given string.
    #- *Input*: "Hello"
    #- *Output*: "Number of vowels: 2"


str = input("Enter a string:")
vowels="aeiouAEIOU"
count=0

for char in str:
  if char in vowels:
     count += 1

print("Number of vowels in the string:", count)