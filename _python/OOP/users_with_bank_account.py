class BankAccount:
    def __init__(self,balance = 0): 
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

birrro = BankAccount(10000)
bob = BankAccount(500)
abuElBir = BankAccount()

class user:
    def __init__(self,name,account):
        self.name = name
        self.account = account
        
    def deposit(self,amount):
        self.account.deposit(amount)
        return self
        
    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self

    def display_user_info(self):
        print("user name : {},".format(self.name),end=" ")
        self.account.display_account_info()
        return self

    def transfer_money(self,other_user,amount):
        self.account.withdraw(amount)
        other_user.deposit(amount)
        return self

bara = user("bara",birrro)
bara.deposit(10).display_user_info()

bara = user("Bara Salameh",bob)
bara.display_user_info()

bara = user("Bara Salameh",abuElBir)
bara.deposit(5000).display_user_info()