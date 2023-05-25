#!/bin/python


class Debug:
  'Debug Class to add debug logs'
  debugfd  = -1 

  def __init__(self, logFile):
    Debug.debugfd = open(logFile, 'w')
    print "Debug File Open."

  def debugLog(self, debug):
    Debug.debugfd.write("{}\n".format(debug)) 

  def __del__(self):
    Debug.debugfd.close()
    print "Debug File Closed."
 

def main():
  debugObj = Debug("debug.log")
  debugObj.debugLog("****test****")


if __name__ == "__main__":
  main()

