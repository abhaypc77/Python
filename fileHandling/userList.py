#!/bin/python


fileName = "/etc/passwd"
userFile  = "users.txt"

with open(fileName, "r") as fobj, open(userFile, 'w') as outFileObj:
  for line in fobj:
    tokens = line.split(':')
    print tokens[0]
    outFileObj.write("%s\n" % tokens[0])
