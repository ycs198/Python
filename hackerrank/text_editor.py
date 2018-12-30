ops = int(raw_input())

s = ""
L = []
for op in xrange(ops):
    print L
    print s
    task = raw_input().split()
    if (task[0] == "1"):
        L.append(s)
        s += task[1]
    elif (task[0] == "2"):
        L.append(s)
        s = s[:len(s) - int(task[1])]
    elif (task[0] == "3"):
        print s[int(task[1]) - 1]
    elif (task[0] == "4"):
        s = L.pop()
