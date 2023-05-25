#!/bin/python

import argparse
from Debug import Debug

class Sort:
  inFile = ''
  outFile = ''

  def __init__(inFile, outFile):
    Sort.inFile = inFile
    Sort.outFile = outFile

  def sortFile():
      



def parseArg():

  parser = argparse.ArgumentParser(description='Sort arguments')  
  
  parser.add_argument('-i', '--input', required=True, help='Input File')
  parser.add_argument('-o', '--output', help='output File')
  parser.add_argument('-d', '--debug', type=int, default=0, help='Debug Flag')
  parser.add_argument('-l', '--log', help='Log File')

  return parser.parse_args()

def main():
 
  args = parseArg()
 
  debug = Debug("debug.log")
  debug.debugLog("Inside Main Method.")
  debug.debugLog(str(args))


  unsortedFile = args.input
  sortedFile = args.output
  debugFlag = args.debug
  logFile = args.log

  if not sortedFile:
    sortedFile = "{}.sorted".format(unsortedFile)

  if not debugFlag and logFile:
    debugFlag = 1

  if not logFile and debugFlag:
    logFile = "debug.log"

  if debugFlag:
    debug.debugLog("Unsorted File = {}, Sorted File = {}, Debug Flag = {}, Log file = {}".format(unsortedFile, sortedFile, debugFlag, logFile))


  sort = Sort(unsortedFile, sortedFile)  
  sort.sortFile()




  print args


if __name__ == "__main__":
  main()
