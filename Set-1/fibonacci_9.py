#9. Write a Python function that generates the first n numbers in the Fibonacci sequence.
 #   - *Input*: 5
  #  - *Output*: "[0, 1, 1, 2, 3]"

def fibonacci(n):
   if n==0:
      return []
   elif n==1:
      return [0]
   
   fibo=[0,1]

   while len(fibo)<n:
      nex=fibo[-1]+fibo[-2]
      fibo.append(nex)

   return fibo
   
print(fibonacci(10))