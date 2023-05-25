#!/bin/python




class jsonParser():
  def __init__(self, json):
    self.json = ''.join(json)
    #self.json = json
    print 'self.json = ', self.json
    self.jsonDict = dict()
    self.curidx = 0
    self.endidx = len(json)

  

  def parseJson(self):
    print 'Inside parseJson', self.json[self.curidx]
    if self.json[self.curidx] == '{':
      self.curidx += 1 
      self.parseJsonObj()
 
  def remSpace(self):
    while 1:
      if self.json[self.curidx] == ' ' or self.json[self.curidx] == '\t' or self.json[self.curidx] == '\n':
        self.curidx += 1
        continue
      else :
        return

  def parseJsonObj(self):
    self.remSpace()
    print 'Inside parseJsonObj'
    if self.json[self.curidx] != '\"':
      print 'Error in parsing'
      return
    self.curidx += 1

    objKey = self.getObjKey()
    self.remSpace()

    print 'self.json[self.curidx] = ', self.json[self.curidx]
    if self.json[self.curidx] != ':':
      print 'Error in parsing'
      return
   
    self.curidx += 1
    self.remSpace()

    if self.json[self.curidx] == '{':
      self.jsonDict[objKey] = dict()
      parseJsonObj()

    else:
      objValue = self.getObjValue()

    self.jsonDict[objKey] = objValue
    
    self.remSpace()
    

     
  def getObjKey(self):

    endquoteidx = self.json[self.curidx:].index('\"')

    print 'self.curidx =', self.curidx
    print 'endquoteidx =', endquoteidx

    objKeyStr = self.json[self.curidx: self.curidx + endquoteidx]
    print 'objKeyStr = ', objKeyStr
    self.curidx += len(objKeyStr)
    self.curidx += 1
    return objKeyStr

  def getObjValue(self):
    endidx = self.json[self.curidx:].index(',')
    if endidx 



    objKeyValue = self.json[self.curidx:self.json[self.curidx:].find('}')]
    print 'objKeyValue = ', objKeyValue
    self.curidx += len(objKeyValue)    
    return objKeyValue



def main():
  with open('example1.json', 'r') as fobj:
    json = fobj.readlines()

  parser = jsonParser(json)
  parser.parseJson()
  

if __name__ == '__main__':
  main()
