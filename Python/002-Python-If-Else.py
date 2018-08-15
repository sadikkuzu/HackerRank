#!/bin/python

# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(raw_input())
if N % 2 == 1:
    print "Weird"
else:
    if N in xrange(6, 21):
        print "Weird"
    else:
        print "Not Weird"
