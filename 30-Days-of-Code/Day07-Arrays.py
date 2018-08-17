# https://www.hackerrank.com/challenges/30-arrays

#!/bin/python
import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(raw_input())

    arr = map(int, raw_input().rstrip().split())
    print ' '.join(str(x) for x in reversed(arr))