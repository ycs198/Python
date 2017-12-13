ab = { 'bala':'bala@me.com',
       'krishna':'krishna@me.com',
       'soura':'soura@me.com'
     }
print "bala address is",ab['bala']
del ab['soura']
print '\n There are {} contacts in the address book \n'.format(len(ab))

for name,address in ab.items():
    print 'contact {} at {}' .format(name,address)

ab['Guido'] = 'guido@python.org'

if 'Guido' in ab:
    print "\n Guido address is",ab['Guido']

print "The complete Dict is:",ab
