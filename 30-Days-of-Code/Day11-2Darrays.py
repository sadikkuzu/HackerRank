# !/bin/python
# https://www.hackerrank.com/challenges/30-2d-arrays
import math
import os
import random
import re
import sys


def hg(arr, r, c):
    s = 0 - arr[r + 1][c] - arr[r + 1][c + 2]
    for i in xrange(3):
        for j in xrange(3):
            s += arr[r + i][c + j]
    return s


if __name__ == '__main__':
    arr = []

    for _ in xrange(6):
        arr.append(map(int, raw_input().rstrip().split()))

    m = set([])
    for x in xrange(4):
        for y in xrange(4):
            m.add(hg(arr, x, y))

    print max(m)