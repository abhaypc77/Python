#!/bin/python

my_tuple = (1, 2, "abc", "xyz", 5, 6)

print "Items in tuple are : ", my_tuple
print "First item in tuple is : ", my_tuple[0]
print "second item in tuple is :", my_tuple[1]
print "First three items in tuple are :", my_tuple[:3]
print "items after first two are :", my_tuple[2:]
print "New items in tuple are :", my_tuple

your_tuple = (7, 8, 9)
our_tuple = my_tuple + your_tuple

print "Items after adding :", our_tuple
#Tuples are immutable
#my_tuple[2] = "pqr"
#my_tuple[3] = 4
