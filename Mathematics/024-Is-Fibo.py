#!/bin/python

fib = list()
fib.append(0)
fib.append(1)

def add_fib():
    global fib
    fib.append(fib[-2] + fib[-1])


# Complete the solve function below.
def solve(n):
    global fib
    while n > max(fib):
        add_fib()
    if n in fib:
        return "IsFibo"
    return "IsNotFibo"