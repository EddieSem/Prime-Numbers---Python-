"""
prime numbers are those numbers who are greator than 1 and are only divisible by 1 or by themselves
"""

# this programs checks if given number is prime or not

num = int(input("Enter a number: "))
if num > 1:
  
   for i in range(2,num):
       if (num % i) == 0:
           break
   else:
       print(num,"is a prime number")

else:
   print(num,"is not a prime number")
