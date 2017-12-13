def UpperCase(str):
    char = ""
    for i in str:
        if i.islower():
            i = i.upper()
        else:
            i = i.lower()
        char = char + i
    return char

print UpperCase(str(raw_input('enter the string:')))
