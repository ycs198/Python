n = int(raw_input())
bala = map(int,raw_input().strip().split(' '))
def area(max_area):
    return len(max_area)*min(max_area)

maximum_list=[area(bala[i:j]) for i in range(len(bala)) for j in range(len(bala),i,-1)]
print max(maximum_list)
