#!/bin/python

import sys

argCount = len(sys.argv)

if argCount < 2:
  print "Usage: {} <Start Table> <End Table>".format(sys.argv[0])
  exit(0)


startTable = int(sys.argv[1])

if argCount == 3:
  endTable = int(sys.argv[2])
else:
  endTable =startTable + 4


for tableNo in range(startTable, endTable+1):
  print "\n\n******Table of {}*****".format(tableNo)
  for i in range(1,11):
    print "{} * {} = {}".format(tableNo, i, tableNo*i)
