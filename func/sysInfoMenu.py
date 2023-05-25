#!/bin/python 

import os 

def showSysInfo():
  print '===========================Sys Info========================'
  os.system("uname -a")
  print '==========================================================='

def showUptime():
  print '=======================Uptime=================='
  os.system("uptime") 
  print '==============================================='
  
def showDiskInfo():
  print '=================Disk-Info====================='
  os.system("df -h") 
  print '==============================================='
  
def showMemInfo():
  print '====================Mem Info======================'
  os.system("free -m") 
  print '=================================================='


while True:
  print "\n\n   Main Menu"
  print "   ========="
  print "1. Sys Info"
  print "2. Uptime"
  print "3. Disk Info"
  print "4. Memory Info"
  print "5. Exit"
  choice = int(raw_input("\nEnter your choice..."))

  if choice == 1:
    showSysInfo()
  elif choice == 2:
    showUptime() 
  elif choice == 3:
    showDiskInfo()
  elif choice == 4:
    showMemInfo()
  elif choice == 5:
    exit(0)
   
  raw_input("\nPress Enter to continue...")






