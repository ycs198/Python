number = 23
running = True

while running:
    bala = int(raw_input("enter the integer:"))
    if bala == number:
        print "congrats,you guessed it"
        running = False
    elif bala < number:
        print "No its little higher than that."
    else:
        print "No its little lower than that."
else:
    print "while loop is over"
print "done"
