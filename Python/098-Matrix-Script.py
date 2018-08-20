#!/bin/python
# https://www.hackerrank.com/challenges/matrix-script/
import math
import os
import random
import re
import sys

nm = raw_input().split()

n = int(nm[0])
m = int(nm[1])

matrix = []

for _ in xrange(n):
    matrix_item = raw_input()
    matrix.append(matrix_item)
txt = ''
for i in xrange(m):
    for j in xrange(n):
        txt += matrix[j][i]

print(re.sub(r'(?<=\w)([^\w\d]+)(?=\w)', ' ', txt))
