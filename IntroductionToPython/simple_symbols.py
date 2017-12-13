def SimpleSymbols(str):
    for i in str:
        if str.isalpha():
            if i-1 == '+':
                if i+1 == '+':
                    print 'True'
        else:
            print 'false'

print SimpleSymbols(str(raw_input('enter the string:')))
