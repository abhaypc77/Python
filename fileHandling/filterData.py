#!/bin/python

'''
Script to Filter specific Logs from 
main.log File
'''

baseFile = "main.log"
newFile = "filter.log"

'''Filter Mask
key = Module Name
value = corresponding Log in Log file
'''
filter = {
'Telephony' : 'TelephonyManager',
'ImsCM'     : 'ImsConnectionManager',
'imsSer'    : 'ImsService',
'imsReg'    : 'ImsRegister',
'adapter'   : 'Adapter',
'Service'   : 'VoWifiService',
'Ike'       : 'SECURITY IKE',
'ipsec'     : 'JuIpsecServer',
'lemon'     : 'LEMON'
}


def filterFile(inFile, outFile):
  keys = filter.keys()
  with open(inFile) as inFileObj, open(outFile, 'w') as outFileObj:
    for line in inFileObj:
      for key in keys:
        if filter[key] in line:
          print line
          outFileObj.write(line)
          break  


def main():

  #TODO Argument parsing
  #parseArg()
  filterFile(baseFile, newFile)


if __name__ ==  '__main__':
  main()

