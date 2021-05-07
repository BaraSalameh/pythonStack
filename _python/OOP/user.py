#  If you've been following along, you're going to utilize the User class we've been discussing for this assignment.

#  For this assignment, we'll add some functionality to the User class:

#  make_withdrawal(self, amount) - have this method decrease the user's balance by the amount specified
#  display_user_balance(self) - have this method print the user's name and account balance to the terminal
#  eg. "User: Guido van Rossum, Balance: $150
#  BONUS: transfer_money(self, other_user, amount) - have this method decrease the user's balance by the amount and 
#  add that amount to other other_user's balance

class user:
    def __init__(self,name,balance = 1000):
        self.name = name
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount
        print("deposit success, current balance : ${}".format(self.balance))
        print("")

    def make_withdrawal(self, amount):
        if(self.balance < amount):
            print("withdrawal operation is denied, not enough balance!")
            print("")
        else:
            self.balance -= amount
            print("withdrawal success, remaining balance : ${}".format(self.balance))
            print("")

    def display_user_balance(self):
        print("user name : {}, balance : ${}".format(self.name,self.balance))
        print("")

    def transfer_money(self,other_user,amount):
        self.make_withdrawal(amount)
        other_user.deposit(amount)

bara = user("bara",50000)
bara.deposit(25000)
bara.deposit(30000)
bara.deposit(10000)
bara.make_withdrawal(100000)
bara.display_user_balance()

khalil = user("khalil")
khalil.deposit(500)
khalil.deposit(300)
khalil.make_withdrawal(1000)
khalil.make_withdrawal(200)
khalil.display_user_balance()

dara = user("Dara",300)
dara.deposit(1000)
dara.make_withdrawal(700)
dara.make_withdrawal(500)
dara.make_withdrawal(200)
dara.display_user_balance()

bara.transfer_money(dara,10000)
bara.display_user_balance()
dara.display_user_balance()


