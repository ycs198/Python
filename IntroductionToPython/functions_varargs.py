def total(inital=5,*numbers,**keywords):
    count = inital
    for number in numbers:
        count += number
    for key in keywords:
        count += keywords[key]
    return count

#s = int(raw_input("enter the numbers"))

print total(int(raw_input("enter the parameter1:")),int(raw_input("enter the parameter2:")),int(raw_input("enter the parameter3:")),vegatables=50,fruits=100)
