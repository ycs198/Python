shoplist = ['apple','mango','carrot','banana']

print 'I have',len(shoplist),'to buy'

print "These items are:",
for item in shoplist:
    print item,

print '\n need to buy the rice too'
shoplist.append('rice')
print '\n now my shopinglist is',shoplist
shoplist.sort()
print '\n my shopping list is now sorted',shoplist
print '\n The firsr item i need to buy is',shoplist[0]
olditem = shoplist[0]
del shoplist[0]
print '\n i dont need that item',olditem
print 'My shopping list is now',shoplist
