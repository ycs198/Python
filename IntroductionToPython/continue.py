while True:
    s = raw_input('enter the string:')
    if s == 'quit':
        break
    if len(s) < 3:
        print 'it is too small'
        continue
print 'input is of good length'

