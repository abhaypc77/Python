#!/bin/python

my_list = [1, 2, "abc", "xyz", 5, 6]
print "Items in list are : ", my_list
print "First item in list is : ", my_list[0]
print "second item in list is :", my_list[1]
print "First three items in list are :", my_list[:3]
print "items after first two are :", my_list[2:]

#Lists are mutable
my_list[2] = "pqr"
my_list[3] = 4

print "New items in list are :", my_list
