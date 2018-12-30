def remove_redundency(x):
    a = ''
    for i in x:
        if i not in a:
            a=a+i
    return a

Name = str(raw_input('enter the the string:'))
factor = int(raw_input('enter the factor:'))
for i in range(len(Name)/factor):
    print remove_redundency(Name[i*factor:factor*(i+1)])
