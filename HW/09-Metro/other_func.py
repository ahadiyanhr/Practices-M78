import os
import pickle
import exceptions as ex 
from User import User
from BankAccount import BankAccount

from MetroCard import CreditCard, LimitedCard, MetroCard, SingleCard


main_menu = '''\nPlease select your option:
        Quit -> 0
        User/Admin Register -> 1
        Account Management -> 2
        Take a Trip -> 3
        Trip Managment (by admin) -> 4
            
            Enter your choice >> '''

acc_manage = '''\nPlease select your option:
        Bank Account Management -> 1
        Metro Card Management -> 2
            
            Enter your choice >> '''

bank_acc_selection = '''\nPlease select your method:
        Balance -> 1
        Deposit -> 2
        Withdraw -> 3
            
            Enter your choice >> '''
           
card_selection = '''\nPlease select type of card:
        Credit Card -> 1
        Limited Card -> 2
        Single Card -> 3
            
            Enter your choice >> '''
            
card_func_selection = '''\nPlease select your method:
        Buy a New Card -> 1
        Charge the Card -> 2
            
            Enter your choice >> '''
            
def search_auth_code(auth_code): # func. for search auth_code between accounts
    for account in BankAccount.owner_accounts.values():
        if BankAccount._check_auth_code(account, auth_code):
            return account
    return False

def get_owner(auth_code): # func. for get user by auth_code
    for user in User.users:
        print(user)
        if user.auth_code == auth_code:
            return user
    return False


def bank_account_manage(select, account, auth_code):
    if select == '1': # Get account  balance
        print(f"Balance: {account.balance}")
    elif select == '2': # Deposit
        amount = int(input("Enter Amount (IRR): "))
        account.deposite(amount, auth_code)
        print(f"New balance: {account.balance}")
    elif select == '3': # Withdraw
        amount = int(input("Enter Amount (IRR): "))
        account.withdraw(amount, auth_code)
        print(f"New balance: {account.balance}")
    else:
        print("Your choice is not valid!")
    return True


def metro_card_manage(card_select, method_select, account, auth_code):
    user = get_owner(auth_code)
    if card_select == '1': # Credit Card
        os.system("cls")
        if method_select == '1': # Buy
            CreditCard(user)
        elif method_select == '2': # Charge
            for card in MetroCard.owner_cards[user]:
                if card[1] == "CreditCard":
                    amount = int(input("Enter amount in IRR: "))
                    card[0].charge(amount, auth_code)
                    input(f"New Card Balance is: {card[0].balance}. Press any key to continue.")
        else:
            print("Your choice is not valid!")
            
    elif card_select == '2': # Limited Card
        os.system("cls")
        if method_select == '1': # Buy
            LimitedCard(user)
        elif method_select == '2': # Charge
            for card in MetroCard.owner_cards[user]:
                if card[1] == "LimitedCard":
                    amount = int(input("Enter amount in IRR: "))
                    card[0].charge(amount, auth_code)
                    input(f"New Card Balance is: {card[0].balance}. Press any key to continue.")
        else:
            print("Your choice is not valid!")
                        
    elif card_select == '3': # Single Card
        os.system("cls")
        if method_select == '1': # Buy
            SingleCard(user)
        elif method_select == '2': # Charge
            input(f"Single Cards can not charge! Press any key to continue.")
        else:
            print("Your choice is not valid!")
            
    else:
        print("Your choice is not valid!")
    return True

def unpickling():
    try:
        with open('users.pickle', 'rb') as up:
            User.users = pickle.load(up)
        with open('cards.pickle', 'rb') as cp:
            MetroCard.owner_cards = pickle.load(cp)
        with open('trips.pickle', 'rb') as tp:
            Trip._trip_records = pickle.load(tp)
    except:
        pass