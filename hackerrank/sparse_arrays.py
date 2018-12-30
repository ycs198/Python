def matchingStrings(strings, queries):
    count = []
    for query in queries:
        count_mine = 0
        for star in strings:
            if query == star:
                count_mine = count_mine + 1
        count.append(count_mine)
    return count


strings_list=[]
for i in range(int(raw_input())):
    strings_list.append(raw_input().strip())
queries_list=[]
for j in range(int(raw_input())):
    queries_list.append(raw_input().strip())

for k in matchingStrings(strings_list,queries_list):
    print k
