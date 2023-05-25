#!/bin/python

import argparse
import sys

parser = argparse.ArgumentParser(description='close bug')

parser.add_argument('-v', '--verbose',
    action="store_true",
    help="verbose output" )

parser.add_argument('-s',
    default="closed",
    choices=['closed', 'wontfix', 'notabug'],
    help="bug status")

parser.add_argument('bugnum',
    type=int,
    help="Bug number to be closed")

parser.add_argument('message',
    nargs='*',
    help="optional message")

args = parser.parse_args()

print("~ Bug Num: {}".format(args.bugnum))
print("~ Verbose: {}".format(args.verbose))
print("~ Status : {}".format(args.s))
print("~ Message: {}".format(" ".join(args.message)))
