def print_max(a,b):
    if a>b:
        print a, 'is max'
    elif a==b:
        print a, 'is equal to',b
    else:
        print b, 'is max'


number1 = int(raw_input('enter the number:'))
number2 = int(raw_input('enter the other number:'))
print_max(number1,number2)
