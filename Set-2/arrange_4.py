### **Arrange string characters such that lowercase letters should come first**

#Given string contains a combination of the lower and upper case letters. Write a program to arrange the characters of a string so that all lowercase letters should come first.

#**Given**:

#```
#str1 = PyNaTive
#```

#**Expected Output**:

#yaivePNT

string = "PyNaTive"
s1=""
s2=""
for ele in string:
    if ele.isupper(): 
        s1+=ele
    else: 
        s2+=ele

s3=s2+s1
print(s3)