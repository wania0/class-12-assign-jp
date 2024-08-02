""" 
Part 1: Introduction to the Base Class
Understanding BankAccount:

Task: Create a base class called BankAccount with the following attributes and methods:

Attributes:
balance: The initial amount of money in the account.
name: The name of the account.

Methods:
get_balance: Print the current balance.
deposit: Add a specified amount to the balance.
withdraw: Subtract a specified amount from the balance if sufficient funds are available.
transfer: Transfer a specified amount to another account."""

# part 1 solution :

class BankAccount:
    
    def __init__(self, balance, account_name):
        self.balance = balance
        self.account_name = account_name

    def get_balance(self):
        print(f"{self.account_name}'s balance is ${self.balance}")

    def deposit(self, amount_deposit):
        if amount_deposit > 0:
            self.balance = self.balance + amount_deposit
            print(f"${amount_deposit} is deposited in {self.account_name}")
        else:
            print("Deposit amount must be greater than zero.")

    def withdraw(self, amount_withdraw):
        if amount_withdraw <= 0:
            print("Withdrawal amount must be greater than zero.")
        elif amount_withdraw > self.balance:
            print(f"Sorry, account {self.account_name} only has a balance of ${self.balance}")
        else:
            self.balance = self.balance - amount_withdraw
            print(f"${amount_withdraw} withdrawn from {self.account_name}")

    def transfer_amount(self, amount, target_account):
        if amount <= 0:
            print("Transfer amount must be greater than zero.")
        elif amount > self.balance:
            print(f"Sorry, account '{self.account_name}' only has a balance of ${self.balance}")
        else:
            self.balance = self.balance - amount
            target_account.balance = target_account.balance + amount
            print(f"${amount} is transferred to {target_account.account_name}")

Dave = BankAccount(1000, "Dave")
Sara = BankAccount(2000, "Sara")

Dave.get_balance()  # should display $1000
Sara.get_balance()  # should display $2000

Sara.deposit(500)   # add 500 in Sara's account
Sara.get_balance()  # should display $2500

Dave.withdraw(10000)  # it should raise an error saying "Sorry, account 'Dave' only has a balance of $1000"
Dave.withdraw(10)     # should subtract $10 from Dave's account
Dave.get_balance()    # should display $990

Dave.transfer_amount(10000, Sara)  # it should raise an error saying "Sorry, account 'Dave' only has a balance of $990"
Dave.transfer_amount(100, Sara)    # should add $100 to Sara's account and remove $100 from Dave's account

Dave.get_balance()  # should display $890
Sara.get_balance()  # should display $2600

# PART 2
# Every InterestRewardsAcct user always receive 5% reward on adding more money

# part 2 solution :

class InterestRewardsAcct(BankAccount):
    
    def deposit(self, amount_deposit):
        if amount_deposit > 0:
            reward = amount_deposit * 0.05
            total = amount_deposit + reward
            self.balance += amount_deposit + reward
            print(f"${total} is deposited in {self.account_name}")
        else:
            print("Deposit amount must be greater than zero.")
    
Jim = InterestRewardsAcct(1000, "Jim")

Jim.get_balance()

Jim.deposit(100) # it should add $100 + Reward amount of extra 5% i.e (%100 * 1.05)

Jim.get_balance() # it should display $1105

Jim.transfer_amount(100, Dave) # should add $100 to Dave account and remove $100 from Jim's account

Jim.get_balance() # it should display $1005.00

# PART 3
# Every SavingsAcct user always receive 5% reward on adding more money
# Every SavingsAcct user always get panelty of $5 on reducing the money

# part 3 solution :

class SavingsAcct(InterestRewardsAcct):
    
    def withdraw(self, amount_withdraw):
        if amount_withdraw <= 0:
            print("Withdrawal amount must be greater than zero.")
        elif amount_withdraw > self.balance:
            print(f"Sorry, account {self.account_name} only has a balance of ${self.balance}")
        else:
            total_withdraw = amount_withdraw + 5
            self.balance -= total_withdraw
            print(f"${total_withdraw} withdrawn from {self.account_name}")
            
    def transfer_amount(self, amount, target_account):
        if amount <= 0:
            print("Transfer amount must be greater than zero.")
        elif amount > self.balance:
            print(f"Sorry, account '{self.account_name}' only has a balance of ${self.balance}")
        else:
            self.balance -= amount + 5
            target_account.balance += amount
            print(f"${amount} is transferred to {target_account.account_name}")
    
    
Blaze = SavingsAcct(1000, "Blaze")

Blaze.get_balance() # it should display $1000

Blaze.deposit(100)   # it should add $100 + Reward amount of extra 5% i.e (%100 * 1.05)
Blaze.get_balance()  # should display $1105 (instead of 1100)

Blaze.withdraw(10)   # should subtract $15 (instead of $10) from Blaze's account
Blaze.get_balance()  # should display $1090 (instead of 1095)

Blaze.transfer_amount(10000, Sara) # it should raise an error saying "Sorry, account 'Blaze' only has a balance of $1090"
Blaze.transfer_amount(1000, Sara) # it should add $1000 to Sara's account and subtract $1005 from Blaze account (instead of $1000)
Blaze.get_balance()  # should display $85
Sara.get_balance()