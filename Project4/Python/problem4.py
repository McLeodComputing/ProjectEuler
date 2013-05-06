#!/usr/bin/python

def isPalindrome(n):
  if n == int(str(n)[::-1]):
    return True
  return False

answer = 1

for i in range(1,999):
  for j in range(1,999):
    test = i*j
    if isPalindrome(test):
      if test > answer:
        answer = test
    j -= 1
  i -= 1

print answer
