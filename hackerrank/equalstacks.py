# Enter your code here. Read input from STDIN. Print output to STDOUT
n1, n2, n3 = map(int, raw_input().split())
s1 = map(int, raw_input().split())
s2 = map(int, raw_input().split())
s3 = map(int, raw_input().split())

h1 = sum(s1)
h2 = sum(s2)
h3 = sum(s3)

while (sum([h1, h2, h3]) > 0):
    if h1 == h2 == h3:
        print h1
        break
    if h1 == max([h1, h2, h3]):
        h1 -= s1.pop(0)
    elif h2 == max([h1, h2, h3]):
        h2 -= s2.pop(0)
    elif h3 == max([h1, h2, h3]):
        h3 -= s3.pop(0)

if h1 == h2 == h3 == 0:
    print 0
