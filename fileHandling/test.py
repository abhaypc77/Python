#!/usr/bin/python

file = "file.txt"
lines = []

with open(file, 'r') as readFileObj:
  line = readFileObj.readline()
  while line:
    print line 
    lines.append("[%s] %s" % ("PREFIX", line))
    line = readFileObj.readline()
  
print lines 