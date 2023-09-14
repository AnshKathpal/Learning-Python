#7.  Write a Python function that checks whether a given number is a prime number.
 #   - *Input*: 13
  #  - *Output*: "13 is a prime number."


def isPrime(num):
   if num<=1:
      return False
   for  i in range(2,int(num**0.5+1)):
      if num%i==0:
       return False
      return True
print(isPrime(9))
