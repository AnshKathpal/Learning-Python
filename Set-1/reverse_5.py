#5. Write a Python function that takes a string and returns the string in reverse order.
 #   - *Input*: "Python"
  #  - *Output*: "nohtyP"


def reversestring(inputstring):
    return inputstring[::-1]


string = "Python"
revstring = reversestring(string)
print(revstring)
