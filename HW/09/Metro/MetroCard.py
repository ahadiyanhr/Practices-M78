import logging
import exceptions as ex
import pickle
from abc import ABC, abstractclassmethod

from User import User
from BankAccount import BankAccount

# Logging Setup:
log_format = "%(asctime)s %(name)s %(levelname)s: %(message)s"
logging.basicConfig(filename= 'metro.log', filemode= 'a',\
    level= logging.DEBUG, format= log_format)

class MetroCard(ABC):
    
    owner_cards = {} # keys: owners, values: list of tuple(MatroCard, "Type")
    
    @abstractclassmethod
    def __init__(self, owner: User, balance: int = 0):
        self.owner = owner
        self.balance = balance
        
class CreditCard(MetroCard):
    
    def __new__(cls, *args):
        if args[0] in MetroCard.owner_cards.keys():
            for value_list in MetroCard.owner_cards.values():
                for card in value_list:
                    if card[1] == "CreditCard":
                        logging.log(logging.ERROR, "This user had a Credit Card already.")
                        raise ex.InstantiateError("This user had a Credit Card already.") 
        return super(CreditCard, cls).__new__(cls)
    
    def __init__(self, owner: User, balance: int = 0):
        self.owner = owner
        self.balance = balance
        if owner in MetroCard.owner_cards:
            MetroCard.owner_cards[owner].append(self, "CreditCard")
        else:
            MetroCard.owner_cards[owner] = [(self, "CreditCard")]
        with open('cards.pickle', 'wb') as ap:
            pickle.dump(MetroCard.owner_cards, ap)
        logging.log(logging.INFO, f"The Credit Card belongs to {owner.auth_code} is created.")
        
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
        if balance < 0:
            logging.log(logging.ERROR, f"Balance of Metro Card is less than Zero.")
            raise ex.CardBalanceError(f"Balance of Metro Card must be more than Zero.")    
        self._balance = balance
    
    def __str__(self):
        return f"{self.owner.auth_code} has a CreditCard with {self.balance} IRR balance."
    
    def _check_auth_code(self, auth_code: str) -> bool:
        '''Check if Authentication Codes are match or not'''
        if self.owner.auth_code == auth_code:
            logging.log(logging.INFO, "The authentication codes are matched.")
            return True
        logging.log(logging.ERROR, "The authentication code was invalid.")
        return False
    
    def _check_balance(self, amount: int) -> bool:
        '''Check if transaction can be done or not'''
        if self.balance < amount:
            logging.log(logging.INFO, "The transaction can not be done due to not enough balance.")
            raise ex.NotEnoughBalance("The transaction is not executable due to not enough balance.")
        return True
    
    def charge(self, amount: int, auth_code: str) -> int:
        if self._check_auth_code(auth_code):
            if BankAccount.owner_accounts[self.owner]._check_balance(amount):
                self.balance += amount
                BankAccount.owner_accounts[self.owner].balance -= amount
                logging.log(logging.INFO, f'{amount}$ was charged. The new CreditCard balance is {self.balance} IRR')
                return self.balance
        logging.log(logging.ERROR, "Charging can not executable!")
        raise ex.ChargeCardError("Charging can not executable!")
    
    def pay_ticket(self, amount: int, auth_code: str) -> int | str:
        
        if self._check_auth_code(auth_code):
            if self._check_balance(amount): # Check the CreditCard balance is enough
                self.balance -= amount
                logging.log(logging.INFO, f"Pay ticket Done! The new CreditCard balance is {self.balance} IRR.")
                return self.balance
        logging.log(logging.ERROR, "Pay ticket can not executable!")
        raise ex.PayTicketError("Pay ticket can not executable!")
    


class LimitedCard(MetroCard):
    
    limit_num = 0
    def __new__(cls, *args):
        if args[0] in MetroCard.owner_cards.keys():
            for value_list in MetroCard.owner_cards.values():
                for card in value_list:
                    if card[1] == "LimitedCard":
                        logging.log(logging.ERROR, "This user had a LimitedCard already.")
                        raise ex.InstantiateError("This user had a LimitedCard already.") 
        return super(LimitedCard, cls).__new__(cls)
    
    def __init__(self, owner: User, balance: int = 0, limit_numbers: int = 2):
        self.owner = owner
        self.balance = balance
        self.limit_numbers = limit_numbers
        self.limit_num = limit_numbers
        if owner in MetroCard.owner_cards:
            MetroCard.owner_cards[owner].append(self, "LimitedCard")
        else:
            MetroCard.owner_cards[owner] = [(self, "LimitedCard")]
        with open('cards.pickle', 'wb') as ap:
            pickle.dump(MetroCard.owner_cards, ap)
        logging.log(logging.INFO, f"The LimitedCard belongs to {owner.auth_code} is created.")
        
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
        if balance < 0:
            logging.log(logging.ERROR, f"Balance of Metro Card is less than Zero.")
            raise ex.CardBalanceError(f"Balance of Metro Card must be more than Zero.")    
        self._balance = balance
        
    @property
    def limit_numbers(self):
        return self._limit_numbers
    
    @limit_numbers.setter
    def limit_numbers(self, limit_numbers: int):
        if limit_numbers < 1:
            logging.log(logging.ERROR, f"Limit Numbers of Card is less than 1.")
            raise ex.LimitedNumbersError(f"Limit Numbers of Card must be equal or more than 1.")    
        self._limit_numbers = limit_numbers
    
    def __str__(self):
        return f"{self.owner.auth_code} has a LimitedCard with {self.balance} IRR balance."
    
    def _check_auth_code(self, auth_code: str) -> bool:
        '''Check if Authentication Codes are match or not'''
        if self.owner.auth_code == auth_code:
            logging.log(logging.INFO, "The authentication codes are matched.")
            return True
        logging.log(logging.ERROR, "The authentication code was invalid.")
        return False
    
    def _check_balance(self, amount: int) -> bool:
        '''Check if transaction can be done or not'''
        if self.balance < amount:
            logging.log(logging.INFO, "The transaction can not be done due to not enough balance.")
            raise ex.NotEnoughBalance("The transaction is not executable due to not enough balance.")
        return True
    
    def charge(self, amount: int, auth_code: str) -> int:
        if self._check_auth_code(auth_code):
            if BankAccount.owner_accounts[self.owner]._check_balance(amount):
                self.balance += amount
                BankAccount.owner_accounts[self.owner].balance -= amount
                logging.log(logging.INFO, f'{amount}$ was charged. The new LimitedCard balance is {self.balance} IRR')
                return self.balance
        logging.log(logging.ERROR, "Charging can not executable!")
        raise ex.ChargeCardError("Charging can not executable!")
    
    def pay_ticket(self, amount: int, auth_code: str) -> int | str:
        if self.limit_num > 0:
            if self._check_auth_code(auth_code):
                if self._check_balance(amount): # Check the CreditCard balance is enough
                    self.balance -= amount
                    self.limit_num -= 1
                    logging.log(logging.INFO, f"Pay ticket Done! The new Limited Number is {self._limit_numbers}.")
                    return self.balance
            logging.log(logging.ERROR, "Pay ticket can not executable!")
            raise ex.PayTicketError("Pay ticket can not executable!")
        MetroCard.owner_cards[self.owner].remove((self, "LimitedCard"))
        with open('cards.pickle', 'wb') as ap:
                pickle.dump(MetroCard.owner_cards, ap)
        logging.log(logging.INFO, "LimitedCard is expired and update the cards.pickle!")
        raise ex.LimitedCardExpired("LimitedCard is expired.")
    

class SingleCard(MetroCard):
    
    _price = 3000
    
    def __new__(cls, *args):
        if args[0] in MetroCard.owner_cards.keys():
            for value_list in MetroCard.owner_cards.values():
                for card in value_list:
                    if card[1] == "SingleCard":
                        logging.log(logging.ERROR, "This user had a SingleCard already.")
                        raise ex.InstantiateError("This user had a SingleCard already.") 
        return super(SingleCard, cls).__new__(cls)
    
    def __init__(self, owner: User):
        if not self._buy:
            logging.log(logging.ERROR, f"The owner bank account's balance is not enough")
            raise ex.NotEnoughBalance("The owner bank account's balance is not enough")
        self.owner = owner
        if owner in MetroCard.owner_cards:
            MetroCard.owner_cards[owner].append(self, "SingleCard")
        else:
            MetroCard.owner_cards[owner] = [(self, "SingleCard")]
        with open('cards.pickle', 'wb') as ap:
            pickle.dump(MetroCard.owner_cards, ap)
        logging.log(logging.INFO, f"The SingleCard belongs to {owner.auth_code} is created.")
        
        
    @property
    def owner(self):
        return self._owner
    
    @owner.setter
    def owner(self, owner: User):
        if not isinstance(owner, User):
            logging.log(logging.ERROR, "The input owner is not a user.")
            raise ex.OwnerInstanceError("The input owner is not a user.")    
        self._owner = owner
       
    def __str__(self):
        return f"{self.owner.auth_code} has a SingleCard."
    
    def _check_auth_code(self, auth_code: str) -> bool:
        '''Check if Authentication Codes are match or not'''
        if self.owner.auth_code == auth_code:
            logging.log(logging.INFO, "The authentication codes are matched.")
            return True
        logging.log(logging.ERROR, "The authentication code was invalid.")
        return False
    
    def _check_balance(self, amount: int) -> bool:
        '''Check if transaction can be done or not'''
        if self.balance < amount:
            logging.log(logging.INFO, "The transaction can not be done due to not enough balance.")
            raise ex.NotEnoughBalance("The transaction is not executable due to not enough balance.")
        return True
    
    def _buy(self, auth_code: str) -> int:
        if self._check_auth_code(auth_code):
            if BankAccount.owner_accounts[self.owner]._check_balance(SingleCard._price):
                BankAccount.owner_accounts[self.owner].withdraw (SingleCard._price,auth_code)
                logging.log(logging.INFO, 'SingleCard was bought.')
                return True
        logging.log(logging.ERROR, "Buy the SingleCard can not executable!")
        raise ex.ChargeCardError("Buy the SingleCard can not executable!")
    
    def pay_ticket(self, auth_code: str) -> bool | str:
        if self._check_auth_code(auth_code):
            MetroCard.owner_cards[self.owner].remove((self, "SingleCard"))
            with open('cards.pickle', 'wb') as ap:
                pickle.dump(MetroCard.owner_cards, ap)
            logging.log(logging.INFO, f"Pay ticket by SingleCard and update the cards.pickle!.")
            return True
        logging.log(logging.ERROR, "Pay ticket can not executable!")
        raise ex.PayTicketError("Pay ticket can not executable!")
