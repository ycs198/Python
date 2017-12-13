name = str(raw_input("enter the string:"))

if name.startswith('bal'):
    print 'the name starts with "bal"'
if 'a' in name:
    print 'Yes it contains "a"'
if name.find('ish') != -1:
    print 'Yes, it contains "ish"'

delimiter = '_*_'

mylist = ['Brazil','Russia','India','china']
print delimiter.join(mylist)
