import logging
import exceptions as ex

from User import User


# Logging Setup:
log_format = "%(asctime)s %(name)s %(levelname)s: %(message)s"
logging.basicConfig(filename= 'metro.log', filemode= 'a',\
    level= logging.DEBUG, format= log_format)

class BankAccount:
    
    owner_accounts = {} # keys: owners, values: accounts of each owner
    minBalance = 500000 # minimum balance, IRR
    fee = 600 # IRR
    
    def __new__(cls, *args):
        if args[0] in BankAccount.owner_accounts.keys():
            logging.log(logging.ERROR, "This user had a bank account already.")
            raise ex.InstantiateError("This user had a bank account already.")
        return super(BankAccount, cls).__new__(cls)
    
    def __init__(self, owner: User, balance: int = minBalance):
        self.owner = owner
        self.balance = balance
        BankAccount.owner_accounts[owner] = self
        logging.log(logging.INFO, f"The bank account belongs to {owner.auth_code} is created.")
        
    @property
    def owner(self):
        return self._owner
    
    @owner.setter
    def owner(self, owner: User):
        if not isinstance(owner, User):
            logging.log(logging.ERROR, f"The input owner is not a user.")
            raise ex.OwnerInstanceError("The input owner is not a user.")    
        self._owner = owner
    
    @property
    def balance(self):
        return self._balance
    
    @balance.setter
    def balance(self, balance: int):
        if balance < BankAccount.minBalance:
            logging.log(logging.ERROR, f"Balance of account is less than 500000 IRR.")
            raise ex.AccountBalanceError("Balance of account must be more than 500000 IRR.")    
        self._balance = balance
    
   
    def __str__(self):
        return f"{self.owner.auth_code} has a bank account with {self.balance}$ balance."
    
    def deposite(self, amount, auth_code):
        if self.owner.auth_code == auth_code:
            self.balance += amount
            logging.log(logging.INFO, f'{amount}$ was diposited. The new account balance is {self.balance}$')
            return self.balance
        else:
            logging.log(logging.ERROR, f"The authentication code was invalid.")
            raise ex.AuthenticationCodeError("The authentication code is invalid!")
        
    def withdrawal(self, amount, auth_code):
        
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
    
    
    
    # def transfer(self, account, amount):
        
    #     # Check the destination account is exist:
    #     if not isinstance(account, BankAccount):
    #         return f'''Transfer failed! There is no any bank account belongs to {account}.'''
        
    #     # Check the acount balance is more than minimum
    #     elif self.balance < BankAccount.minBalance:
    #         minDeposit = round(BankAccount.minBalance-self.balance, 2)
    #         return f'''Transfer failed! The account balance is less than the minimum({BankAccount.minBalance}$).''' 
        
    #     # Check the acount balance is more than minimum after operation and do it
    #     elif ((self.balance-amount) >= BankAccount.minBalance):
    #         self.balance = round(self.balance-amount,2)
    #         account.balance = round(account.balance+amount,2)
    #         return f'''Done! {amount}$ was transfered to {account.ownerName}'s account. The new account balance is {self.balance}$'''
        
    #     # The acount balance is less than minimum after operation
    #     else:
    #         return f'''Transfer is not executable! The account balance will be less than the minimum({BankAccount.minBalance}$) after this operation.'''
            

# hamid = BankAccount('Hamid', 11.1)
# saeed = BankAccount('Saeed', 100)

# print(hamid)
# print(hamid.withdrawal(5))
# print(hamid.withdrawal(10))
# print(hamid.deposite(15))
# print(hamid.withdrawal(5))

# print(saeed)
# print(hamid.transfer(saeed,5))
# print(saeed)
# print(hamid)
# majid = 'Majid'
# print(hamid.transfer(majid,5))
