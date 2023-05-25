#!/bin/python

print "Hello World!"

name = raw_input("Enter Name : ")
emp_id = raw_input("Enter Emp_id : ")

print "Hello {} your Emp id is {}".format(name, emp_id)
print "Hello %s your Emp id is %d" % (name, int(emp_id))
print "Hello", name, "your Emp id is", emp_id
