array_length = int(raw_input())
array_list = [0] * array_length
final_list = []
bala = ' '
print
input_list = raw_input().strip().split()
j = len(input_list) - 1
if j+1 == array_length:
    for i in xrange(j+1):
        final_list.append(input_list[j])
        j = j-1
else:
    print "can't have more items than the number of indexes"

print bala.join(final_list)
