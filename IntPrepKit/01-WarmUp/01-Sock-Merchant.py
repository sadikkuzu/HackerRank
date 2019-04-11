#!/bin/python
# https://www.hackerrank.com/challenges/sock-merchant/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=warmup

import math
import os
import random
import re
import sys


# Complete the sockMerchant function below.
def sock_merchant(n, ar):
    d = dict()
    for i in ar:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    res = 0
    for key, value in d.iteritems():
        res += value/2
    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    ar = map(int, raw_input().rstrip().split())

    result = sock_merchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
