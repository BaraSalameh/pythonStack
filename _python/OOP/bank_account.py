class BankAccount:
    def __init__(self,int_rate,balance = 0): 
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount
        return self

    def withdraw(self,amount):
        if amount > self.balance:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        else:
            self.balance -= amount
        return self

    def display_account_info(self):
        print("Balance : {}".format(self.balance))
        return self

    def yield_interest(self):
        self.balance += self.balance*self.int_rate
        return self

bara = BankAccount(0.05)
khalil = BankAccount(0.01)

bara.deposit(500).deposit(300).deposit(1000).withdraw(1700).yield_interest().display_account_info()
khalil.deposit(1000).deposit(1500).withdraw(2700).withdraw(2000).withdraw(100).withdraw(200).yield_interest().display_account_info()


