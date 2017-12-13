print 'simple assignment'
shoplist = ['apple','mango','carrot','banana']

mylist = shoplist
print 'mylist',mylist

del shoplist[0]

print 'shoplist is',shoplist
print 'mylist is',mylist


print 'copy by making a full slice'

mylist = shoplist
print 'shoplist',shoplist

del mylist[0]


print 'shoplist is',shoplist
print 'mylist is',mylist


