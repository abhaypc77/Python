#!/bin/pyhton

import sys

num_args = len(sys.argv)

if num_args < 4:
  print 'Usage: %s operand1 operator operand2' % (sys.argv[0])
  print '      Allowed operators are +,-,*,/,%'
  exit(1)


oprd1 = int(sys.argv[1])
opr = sys.argv[2]
oprd2 = int(sys.argv[3])

if opr == '+':
  result = oprd1 + oprd2
elif opr == '-':
  result = oprd1 - oprd2
elif opr == '*':
  result = oprd1 * oprd2
elif opr == '/':
  result = oprd1 / oprd2
elif opr == '%':
  result = oprd1 % oprd2
else:
  print 'wrong value of operator\n\tAllowed operators are +,-,*,/,%'
  exit(2)

print 'Result = [%d]' % (result)






 
