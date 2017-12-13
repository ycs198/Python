def CheckNums(num1,num2):
    if num1>num2:
        return True
    elif num2>num1:
        return False
    else:
        return False

print CheckNums(int(raw_input('enter the first number:')),int(raw_input('enter the second number:')))
