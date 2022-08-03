import logging
import exceptions as ex
from abc import ABC, abstractclassmethod

from User import User
from BankAccount import BankAccount

# Logging Setup:
log_format = "%(asctime)s %(name)s %(levelname)s: %(message)s"
logging.basicConfig(filename= 'metro.log', filemode= 'a',\
    level= logging.DEBUG, format= log_format)

# class MetroCard:
    
#     owner_cards = {} # keys: owners, values: list of tuple(MatroCard, "Type")

#     def __new__(cls, *args):
#         return super().__new__(cls)
    
#     def __init__(self, owner: User, balance: int = 0):
#         self.owner = owner
#         self.balance = balance
        
class CreditCard:
    owner_cards = {} # keys: owners, values: list of tuple(MatroCard, "Type")
    
    def __new__(cls, *args):
        if args[0] in CreditCard.owner_cards.keys():
            for card in CreditCard.owner_cards.values():
                if card[1] == "CreditCard":
                    logging.log(logging.ERROR, "This user had a Credit Card already.")
                    raise ex.InstantiateError("This user had a Credit Card already.") 
        return super().__new__(cls)
    
    def __init__(self, owner: User, balance: int = 0):
        self.owner = owner
        self.balance = balance
        CreditCard.owner_cards[owner] = (self, "CreditCard")
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
    
