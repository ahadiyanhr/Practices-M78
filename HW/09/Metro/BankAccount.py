from math import floor
from User import User

class BankAccount:
    
    minBalance = 500000 # minimum balance, IRR
    fee = 600 # IRR
    
    # account attributes:
    def __init__(self, owner: User, balance):
        self.owner = owner
        self.balance = balance
    
    # description of class:    
    def __str__(self):
        
        # If the acount balance is less than minimum
        if self.balance < BankAccount.minBalance:
            minDeposit = round(BankAccount.minBalance-self.balance, 2)
            return f'''Oops! {self.ownerName}'s account balance is less than the minimum({BankAccount.minBalance}$).\nPlease deposit at least {minDeposit}$'''
        return f"{self.ownerName} has a bank account with {self.balance}$ balance."
    
    def withdrawal(self, amount):
        
        # Check the acount balance is more than minimum
        if self.balance < BankAccount.minBalance:
            minDeposit = round(BankAccount.minBalance-self.balance, 2)
            return f'''Withdrawal failed! The account balance is less than the minimum({BankAccount.minBalance}$).''' 
        
        # Check the acount balance is more than minimum after operation and do it
        elif ((self.balance-amount) >= BankAccount.minBalance):
            self.balance = round(self.balance-amount,2)
            return f'''Done! {amount}$ was withdrawn. The new account balance is {self.balance}$'''
        
        # The acount balance is less than minimum after operation
        else:
            return f'''Withdrawal is not executable! The account balance will be less than the minimum({BankAccount.minBalance}$) after this operation.'''
    
    def deposite(self, amount):
        self.balance = round(self.balance+amount,2)
        return f'''Done! {amount}$ was diposited. The new account balance is {round(self.balance,2)}$'''
    
    def transfer(self, account, amount):
        
        # Check the destination account is exist:
        if not isinstance(account, BankAccount):
            return f'''Transfer failed! There is no any bank account belongs to {account}.'''
        
        # Check the acount balance is more than minimum
        elif self.balance < BankAccount.minBalance:
            minDeposit = round(BankAccount.minBalance-self.balance, 2)
            return f'''Transfer failed! The account balance is less than the minimum({BankAccount.minBalance}$).''' 
        
        # Check the acount balance is more than minimum after operation and do it
        elif ((self.balance-amount) >= BankAccount.minBalance):
            self.balance = round(self.balance-amount,2)
            account.balance = round(account.balance+amount,2)
            return f'''Done! {amount}$ was transfered to {account.ownerName}'s account. The new account balance is {self.balance}$'''
        
        # The acount balance is less than minimum after operation
        else:
            return f'''Transfer is not executable! The account balance will be less than the minimum({BankAccount.minBalance}$) after this operation.'''
            

hamid = BankAccount('Hamid', 11.1)
saeed = BankAccount('Saeed', 100)

print(hamid)
print(hamid.withdrawal(5))
print(hamid.withdrawal(10))
print(hamid.deposite(15))
print(hamid.withdrawal(5))

print(saeed)
print(hamid.transfer(saeed,5))
print(saeed)
print(hamid)
majid = 'Majid'
print(hamid.transfer(majid,5))
