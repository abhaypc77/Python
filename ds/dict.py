#!/bin/python

my_dict = {'name' : 'abc', 'emp_id' : 123, 'http' : 80, 'https' : 443}
print "Items in dict are : ", my_dict
print "Name : ", my_dict['name']
print "Emp_id : ", my_dict['emp_id']

new_dict = {'pop3' : 110, 'smpt' : 25}
print "\nAdding items in Dictionary"

my_dict.update(new_dict);
print "Items in dict are : ", my_dict
print "\nUpdatting items in Dictionary"

my_dict['emp_id'] = 321
print "Items in dict are : ", my_dict
print "\nDeleting items in Dictionary"
del my_dict['pop3']
print "Items in dict are : ", my_dict
print "\nKeys in Dict are : %s" % my_dict.keys()
print "values in Dict are : ",str(my_dict.values())

