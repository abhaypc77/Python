#!/bin/python 

import os 

while True:
  print "\n\n   Main Menu"
  print "   *********"
  print "1. Sys Info"
  print "2. Uptime"
  print "3. Disk Info"
  print "4. Memory Info"
  print "5. Exit"
  choice = int(raw_input("\nEnter your choice..."))

  if choice == 1:
    os.system("uname -a")
  elif choice == 2:
    os.system("uptime") 
  elif choice == 3:
    os.system("df -h") 
  elif choice == 4:
    os.system("free -m") 
  elif choice == 5:
    exit(0)







