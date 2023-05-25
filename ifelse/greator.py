#!/bin/python

import sys

num_args = len(sys.argv)

if num_args < 4:
  print "Usage: %s num1 num2 num3" % (sys.argv[0])
  sys.exit(1)


a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

print "First Num = ", a
print "Second Num = ", b
print "Third Num = ", c


if a > b and a > c:
  print "Greatest num = ", a
else:
  if b > a and b > c:
    print "Greatest num = ", b
  else:
    print "Greatest num = ", c
     


