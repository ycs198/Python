from dateutil import parser
if __name__ == '__main__':
    t = int(raw_input())
    for _ in range(t):
        s1 = raw_input()
        s2 = raw_input()
        t1 = parser.parse("Sun 4 May 2015 13:54:36 -0600")
        t2 = parser.parse("Sun 4 May 2015 13:54:36 -0000")
        diff = t1 - t2
        print int(diff.total_seconds())
