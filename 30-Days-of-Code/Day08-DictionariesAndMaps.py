# Enter your code here. Read input from STDIN. Print output to STDOUT
# https://www.hackerrank.com/challenges/30-dictionaries-and-maps
n = int(raw_input())
d = dict()
for _ in xrange(n):
    x = str(raw_input()).split(' ')
    d[x[0]] = x[1]
q = raw_input()
try:
    while(q<>''):
        if q in d:
            print str(q)+"="+str(d[q])
        else:
            print "Not found"
        q = raw_input()
except:
    pass