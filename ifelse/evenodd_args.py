#!/bin/python

import sys

x = int(sys.argv[1])

if (x % 2 == 0):
  print "[%d] is even" % x
else:
  print "[%d] is odd" % x
