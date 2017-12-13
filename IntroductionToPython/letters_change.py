def LetterChanges(str):
    newString = ""
    for i in str:
        if i.isalpha():
            if i.lower() == 'z':
                i = 'a'
            else:
                i = chr(ord(i)+1)
        if i in 'aeiou':
            i = i.upper()
        newString = newString + i

    return newString

print LetterChanges(str(raw_input('enter the string name:')))


