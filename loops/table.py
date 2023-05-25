#!/bin/python

import sys

argCount = len(sys.argv)

if argCount < 2:
  print "Usage: {} <Table No> <Table Limit>".format(sys.argv[0])
  exit(0)

tableNo = int(sys.argv[1])

if argCount == 3:
  tableLimit = int(sys.argv[2])
else:
  tableLimit = 10

for i in range(1, tableLimit+1):
  print "{} * {} = {}".format(tableNo, i, tableNo*i)
