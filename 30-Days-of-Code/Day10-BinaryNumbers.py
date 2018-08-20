#!/bin/python
# https://www.hackerrank.com/challenges/30-binary-numbers/
import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(raw_input())
    x2 = bin(n)[2:]
    for r in reversed(range(1, len(x2)+1)):
        if x2.count('1'*r):
            print r
            break
