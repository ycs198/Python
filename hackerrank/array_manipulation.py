array_len,no_of_ops=raw_input().split(' ')
empty_list = []
for i in range(int(no_of_ops)):
    empty_list.append(raw_input())




def arrayManipulation(array_len, queries):
    zeros_list = [0] * int(array_len)
    for i in queries:
        b = i.split(' ')
        for i in range(int(b[0]),int(b[1])+1):
            zeros_list[i-1] = zeros_list[i-1] + int(b[2])
    return zeros_list


receoived_list = arrayManipulation(int(array_len),empty_list)
temp = 0
for j in range(len(receoived_list)):
    if temp < receoived_list[j]:
        temp = receoived_list[j]

print temp
