class BankAccount:

    all_accounts = []

    def __init__(self, int_rate=0.02, balance=0):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)

    def deposit(self, amt):
        self.balance += amt
        return self
    
    def withdraw(self, amt):
        if self.balance > amt:
            self.balance -= amt
            return self
        else:
            print("insufficient funds: Charging a $5 fee")
            self.balance = self.balance - 5
            return self

    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self

    def yield_interest(self):
        self.balance = self.balance * (1.0 + self.int_rate)
        return self
    
    @classmethod
    def all_accounts_info(cls):
        for one_account in cls.all_accounts:
            one_account.display_account_info()


#user class
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.checking = BankAccount()
        self.savings = BankAccount(4,0)

    def make_deposit(self, amt, acct):
        if acct == 'checking':
            self.checking.deposit(amt)
        elif acct == 'savings':
            self.savings.deposit(amt)
        else:
            print("please specify checking or savings to deposit")
        return self
    
    def make_withdrawal(self, amt=0, acct=" "):
        if acct == 'checking':
            self.checking.withdraw(amt)
        elif acct == 'savings':
            self.savings.deposit(amt)
        else:
            (print("please specify checking or savings to deposit"))
        return self

    
    def display_user_balance(self):
        print(f"Checking Balance: ${self.checking.balance}")
        print(f"Savings Balance: ${self.savings.balance}")
        


user1 = User('Matt', 'coding@dojo.com')

user1.display_user_balance

user1.make_deposit(100)
user1.display_user_balance()
user1.make_withdrawal(50, 'checking')
user1.display_user_balance()