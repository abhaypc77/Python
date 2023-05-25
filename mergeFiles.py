#!/bin/python

'''
Script to Merge main.log file with 
radio.log file
'''

mergedFile = "merged.log"

'''
List of files to be merged
key = File Description
value = FileName
'''
mergeFileList = {
'AP' : 'main.log',
'CP' : 'radio.log',
}

def mergeFiles():
  lines = []
  files = mergeFileList.keys()
 
  for file in files:
    with open(mergeFileList[file], 'r') as readFileObj:
      line = readFileObj.readline()
      while line:
        lines.append("[%s] %s" % (file, line))
        line = readFileObj.readline()
          
  with open(mergedFile, 'w') as mergedFileObj:
    for line in sorted(lines, key=lambda line: line.split()[2]):
      mergedFileObj.write(line)
		   
		   
def main():

  #TODO Argument parsing
  #parseArg()
  mergeFiles()
  

if __name__ ==  '__main__':
  main()

