def SimpleAdd(num):
    result = 0
    for i in range(1,num+1):
        result = result+i
    return result


print SimpleAdd(int(raw_input('enter the number:')))
