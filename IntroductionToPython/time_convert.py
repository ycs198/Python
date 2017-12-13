def TimeConvert(num1):
    num2 = num1 /60
    num3 = num1 % 60
    print num2,":",num3


print TimeConvert(int(raw_input("enter the number:")))
