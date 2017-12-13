def AlphabetSoup(str):
    name = list(str)
    sortedname = sorted(name)
    return "".join(sortedname)


print AlphabetSoup(raw_input("enter the string:"))
