### **Display numbers from a list using loop**

#Write a program to display only those numbers from a [list](https://pynative.com/python-lists/) that satisfy the following conditions

#- The number must be divisible by five
#- If the number is greater than 150, then skip it and move to the next number
#- If the number is greater than 500, then stop the loop

#**Given**:

#```
#numbers = [12, 75, 150, 180, 145, 525, 50]
#```

#**Expected output:**

num_list=[12, 75, 150, 180, 145, 525, 50]

for ele in num_list:
    if ele>500: break
    if ele>150: continue
    if ele%5==0: print(ele)