#!/bin/python

import sys

def sum(x, y):
  return x + y

def sub(x, y):
  return x - y

def mul(x, y):
  return x * y

def div(x, y):
  return x / y


num_args = len(sys.argv)

num1 = int(sys.argv[1])
total = num1
arg = 2

while arg < num_args:
  opr = sys.argv[arg]
  num2 = int(sys.argv[arg + 1])

  if opr == '+':
    total = sum(total, num2)    

  elif opr == '-':
    total = sub(total, num2)    

  elif opr == '*':
    total = mul(total, num2)    
 
  elif opr == '+':
    total = div(total, num2)   
  
  else:
    print 'Wrong Operator'
    exit(1)

  arg = arg + 2

print 'Result = ', total











 
