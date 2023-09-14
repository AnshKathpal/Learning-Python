#8. Write a Python function that calculates the factorial of a number.
 #   - *Input*: 5
  #  - *Output*: "Factorial of 5 is 120."

def factorial(num):
   if num==0 or num==1:
      return 1
   ans=1
   for i in range(2, num+1):
    ans*=i
   return ans
   
print(factorial(5))