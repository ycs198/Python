def maximum(x,y):
    if x > y:
        return x
    elif x == y:
        return 'The Numbers are equal'
    else:
        return y

print maximum(int(raw_input("enter the first number:")),int(raw_input("enter the second number:")))
