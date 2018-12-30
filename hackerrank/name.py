S = raw_input().strip()
S_length = len(S)
print S_length
player1, player2 = 0,0


for i in xrange(S_length):
    print S[i]
    if S[i] in "AEIOU":
        player1 += S_length - i
        print player1
    else:
        player2 += S_length - i
        print player2

if player1 > player2:
    print "Kevin", player1
elif player1 < player2:
    print "Stuart", player2
else:
    print "Draw"
