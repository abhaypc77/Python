#!/bin/python


for num in range(2, 100):
  i = 2
  while i <= num:
    if num % i == 0:
      break;
    else:
      i+=1
  
  if i == num:
    print num
