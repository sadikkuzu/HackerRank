import numpy

N = input()
arr = list()
for i in range(int(N)):
    arr.append(list(map(lambda x: float(x), input().split(' '))))

print(round(numpy.linalg.det(arr),2))
