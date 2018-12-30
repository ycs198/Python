#!/bin/python

import sys


g = int(raw_input().strip())
for a0 in xrange(g):
    n,m,x = raw_input().strip().split(' ')
    n,m,x = [int(n),int(m),int(x)]
    a = map(int, raw_input().strip().split(' '))
    b = map(int, raw_input().strip().split(' '))
    c = [0]
    for e in a:
        c.append(c[-1] + e)
    d = [0]
    for e in b:
        d.append(d[-1] + e)
    a, b = c, d
    ans = 0
    i, j = 0, len(b) - 1
    while i < len(a) and j >= 0:
        if a[i] + b[j] > x:
            print 'no of tmes if block execution'
            j -= 1
        else:
            print 'no of times else block execution'
            ans = max(ans, i + j)
            i += 1

    print ans
