#!/bin/python


fobj = open("file.txt", "r")

lines = fobj.readlines()
print "All lines of file are:\n{}".format(lines)

fobj.close()  

print "-------------------------------"

fobj = open('file.txt', 'r')
for line in fobj:
  print line

print "-------------------------------"


fobj = open("file.txt", "r")
line = fobj.readline()
while line:
  print line
  line = fobj.readline()

fobj.close()  





