class Account(object):
    def __init__(self,name,balance,min_balance):
        self.name = name
        self.balance = balance
        self.min_balance = min_balance


    def deposit(self,amount):
        self.balance += amount

    def withdraw(self,amount):
        if self.balance - amount >= self.min_balance:
            self.balance -= amount
        else:
            print("Sorry,Not enough funds !")

    def statements(self):
        print("Account Balance: ${}".format(self.balance))


class Currnet(Account):
    def __init__(self,name,balance):
        super(Currnet,self).__init__(name,balance,min_balance=-1100)
    def __str__(self):
        return "{}'s Current Account : Balance ${}".format(self.name,self.balance)


class Savings(Account):
    def __init__(self,name,balance):
        super(Savings,self).__init__(name,balance,min_balance=0)
    def __str__(self):
        return "{}'s Savings account : Balance ${}".format(self.name,self.balance)


"""x = Currnet("bala",500)
x.deposit(300)
x.statements()
x.withdraw(800)
x.statements()
x.withdraw(1100)
x.statements()
x.withdraw(1)
print x"""

z = Savings("krishna",500)
z.deposit(300)
z.statements()
z.withdraw(800)
z.withdraw(100)
print z
