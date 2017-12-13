def ChangeLetters(str):
    emptystring = ""
    for i in str:
        if i.isaplha():
            if i.lower() == 'z':
                i = 'a'
            else:
                i = chr(ord(i)+1)
        if i in 'aeiou':
                i = i.upper()
        emptystring = emptystring + i
    return emptystring

print ChangeLetters(str(raw_input('enter the string name:')))


