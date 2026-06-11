class BankAccount:
    def __init__(self,accholder,balance):
        self.accholder=accholder
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
    def withdraw(self,amount):
        if(amount>self.balance):
            raise ValueError("Insufficient Balance")
        self.balance-=amount
    def displaybalance(self):
        print(self.balance)
a=BankAccount("Ruhaan",5000)
a.deposit(500)
a.displaybalance()
a.withdraw(1000)
a.displaybalance()
a.withdraw(10000)
a.displaybalance()
