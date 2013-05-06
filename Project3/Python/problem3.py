#!/usr/bin/python

from math import sqrt

def isPrime(n):
  i=3
  while i < n/2:
    if n%i==0:
      return False
    i += 2

  return True



#Main
n=600851475143
answer = n  #if no other answer is found, the number is the answer 


#starting with the sqrt, work backwards so we can quit as soon as we find the first one 
i=int(sqrt(n))

#ignore even numbers, they are not prime
if i%2==0:
  i -= 1

#start the search
while i > 1:
  if n%i == 0:
    if isPrime(i):
      answer = i
      break

  i -= 2 #ignore even numbers, we know they aren't prime

print answer
      
