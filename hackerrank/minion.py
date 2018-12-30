from collections import Counter
def minion_game(Name):
    length =len(Name)
    vowel_count = 0
    consent_count = 0
    Name_list = []
    for i in xrange(length):
        for j in xrange(length):
            if Name[i:j+1] != '':
                Name_list.append(Name[i:j+1])

    count = Counter(Name_list)

    iter_list = count.keys()
    for i in iter_list:
        if i[0] == 'A' or i[0] == 'E' or i[0] == 'i' or i[0] == 'O' or i[0] == 'U':
            vowel_count = vowel_count + count[i]
        else:
            consent_count = consent_count + count[i]

    if vowel_count > consent_count:
        print "Kevin {}".format(vowel_count)
    elif vowel_count < consent_count:
        print "Stuart {}".format(consent_count)
    elif vowel_count == consent_count:
        print 'DRAW'

if __name__ == '__main__':
    s = raw_input()
    minion_game(s)
