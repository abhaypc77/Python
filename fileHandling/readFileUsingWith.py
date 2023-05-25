#!/bin/python

with open("file.txt", "r") as fobj:
  allLines = fobj.readlines()
 

print "ALL line: {}".format(allLines) 

inFile = "File.txt"
outFile = "outFile.txt"

with open(inFile) as inFileObj, open(outFile, 'w') as outFileObj:
  for line in inFileObj:
    print line
    outFileObj.write(line)

