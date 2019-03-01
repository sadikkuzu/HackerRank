# Complete the pickingNumbers function below.
def picking_numbers(a):
    a.sort()
    d = list()  # differences list
    for i in xrange(len(a) - 1):
        d.append(a[i + 1] - a[i])
    m = list()  # max diffs list
    for i in xrange(len(d)):
        check = {0, 1}
        m.append(1)
        for j in xrange(i, len(d)):
            if d[j] in check:
                m[-1] += 1
                if d[j] == 1:
                    check.remove(1)
            else:
                break
    return max(m)
