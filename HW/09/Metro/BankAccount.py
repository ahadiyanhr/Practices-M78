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
            logging.log(logging.ERROR, "The input owner is not a user.")
            raise ex.OwnerInstanceError("The input owner is not a user.")    
        self._owner = owner
    
    @property
    def balance(self):
        return self._balance
    
    @balance.setter
    def balance(self, balance: int):
        if balance < self.minBalance:
            logging.log(logging.ERROR, "Balance of account is less than 500000 IRR.")
            raise ex.AccountBalanceError("Balance of account must be more than 500000 IRR.")    
        self._balance = balance
    
   
    def __str__(self):
        return f"{self.owner.auth_code} has a bank account with {self.balance} IRR balance."
    
    def _check_auth_code(self, auth_code: str) -> bool:
        '''Check if Authentication Codes are match or not'''
        if self.owner.auth_code == auth_code:
            logging.log(logging.INFO, "The authentication codes are matched.")
            return True
        logging.log(logging.ERROR, "The authentication code was invalid.")
        return False
    
    def _check_balance(self, amount: int) -> bool:
        '''Check if transaction can be done or not'''
        if self.balance < (self.minBalance + self.fee + amount):
            logging.log(logging.INFO, "The transaction can not be done due to not enough balance.")
            raise ex.NotEnoughBalance("The transaction is not executable due to not enough balance.")
        return True
    
    def _check_account(self, account: "BankAccount") -> bool:
        '''Check if account exists or not'''
        if isinstance(account, BankAccount):
            if account in BankAccount.owner_accounts.values():
                return True
            logging.log(logging.ERROR, "The bank account is not exist.")
            raise ex.AccountNotExist("The bank account is not exist.")
        logging.log(logging.ERROR, "The input object is not a Bank Account.")
        raise ex.IsNotBankAccount("The input object is not a Bank Account.")
    
    def deposite(self, amount: int, auth_code: str) -> int:
        if self._check_auth_code(auth_code):
            self.balance += amount
            logging.log(logging.INFO, f'{amount}$ was diposited. The new account balance is {self.balance} IRR')
            return self.balance
        raise ex.AuthenticationCodeError("The authentication code is invalid!")
    
    
    def withdraw(self, amount: int, auth_code: str) -> int | str:
        
        if self._check_auth_code(auth_code):
            if self._check_balance(amount): # Check the account balance is enough
                self.balance -= (amount + self.fee)
                logging.log(logging.INFO, f"Withdrawal Done! The new account balance is {self.balance} IRR.")
                return self.balance
        raise ex.AuthenticationCodeError("The authentication code is invalid!")
    
    
    
    def transfer(self, account: "BankAccount", amount: int, auth_code: str) -> int | str:

        if self._check_account(account) and self._check_auth_code(auth_code):
            if self._check_balance(amount): # Check the account balance is enough
                account.balance += amount
                self.balance -= amount
                logging.log(logging.INFO, f"Transfering Done! The new account balance is {self.balance} IRR.")
                return self.balance
        raise ex.TransferingError(f"Transfer can not executable!")
            
