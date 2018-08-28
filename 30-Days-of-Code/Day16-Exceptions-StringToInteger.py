# https://www.hackerrank.com/challenges/30-exceptions-string-to-integer
#!/bin/python

import sys


S = raw_input().strip()
try:
    print int(S)
except:
    print "Bad String"