def search_for_vowels( phrase ) :
    vowels = { 'a','e','i','o','u'}
    #print (vowels)
    bala = vowels.intersection(set(phrase))
    #print (bala)
    return bala
#print ("calling the function for the first time")
print(search_for_vowels( phrase="balakrishena" ))
