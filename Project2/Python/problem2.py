#!/usr/bin/python

first=1
last=2
answer=2

while last < 4000000:
  next = first + last
  if next%2 == 0:
    answer += next

  first = last
  last = next

print answer
  
