#!/bin/python
import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(raw_input())
    for i in xrange(1, 11):
        print str(n)+" x "+str(i)+" = "+str(n*i)