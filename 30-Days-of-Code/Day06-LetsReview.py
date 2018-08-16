# https://www.hackerrank.com/challenges/30-review-loop

# Enter your code here. Read input from STDIN. Print output to STDOUT
def gezgin(s):
    l = list(s)
    l.reverse()
    k, m = list(), list()
    while(len(l)>0):
        try:
            k.append(l.pop())
            m.append(l.pop())
        except:
            pass
    k = ''.join(k)
    m = ''.join(m)
    print k,m

if __name__ == '__main__':
    n = int(raw_input())
    for _ in xrange(n):
        gezgin(raw_input())