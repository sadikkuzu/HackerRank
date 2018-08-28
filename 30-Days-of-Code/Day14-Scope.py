# https://www.hackerrank.com/challenges/30-scope
class Difference:
    def __init__(self, a):
        self.__elements = a
	# Add your code here
    def computeDifference(self):
        f = set([])
        a = self.__elements
        for i in xrange(len(a)):
            for j in xrange(i, len(a)):
                f.add(abs(a[i] - a[j]))
        self.maximumDifference = max(f)

# End of Difference class

_ = raw_input()
a = [int(e) for e in raw_input().split(' ')]

d = Difference(a)
d.computeDifference()

print d.maximumDifference