#!/bin/python

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    total = round(meal_cost * (1.0 + ((tip_percent+tax_percent)*1.0 / 100)))
    print "The total meal cost is "+str(int(total))+" dollars."

if __name__ == '__main__':
    meal_cost = float(raw_input())

    tip_percent = int(raw_input())

    tax_percent = int(raw_input())

    solve(meal_cost, tip_percent, tax_percent)
