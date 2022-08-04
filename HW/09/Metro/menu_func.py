import exceptions as ex 
from User import User
from Admin import Admin
from BankAccount import BankAccount
from MetroCard import CreditCard, LimitedCard, SingleCard


main_menu = '''\nPlease select your option:
        Quit -> 0
        User/Admin Register -> 1
        Account Management -> 2
        Take a Trip -> 3
        Trip Managment (by admin) -> 4
            
            Enter your choice >> '''

acc_manage = '''\nPlease select your option:
        Bank Account Management -> 1
        Credit Card Management -> 2
            
            Enter your choice >> '''
            
card_func_selection = '''\nPlease select type of card:
        Credit Card -> 1
        Limited Card -> 2
        Single Card -> 3
            
            Enter your choice >> '''
            
def register(): # get information to pass them to User/Admin class
    fn = input('Enter first_name: ')
    ln = input('Enter last_name: ')
    id = input('Enter id_number (must be 10 numbers): ')
    ps = input('Enter Password (must be more than 4 chars): ')
    phi = input('Do you have Phone Number? y/N ')
    if phi in ['', 'n', 'N']:
        ph = None
    else:
        ph = input('Enter Phone Number: ')
    return [fn, ln, id, ps, ph]

def search_auth_code(auth_code): # func. for search auth_code between accounts
    for account in BankAccount.owner_accounts.values():
        if BankAccount._check_auth_code(account, auth_code):
            return account
    return False

def bank_account_manage(account, auth_code):
    select = input('''\nPlease select your method:
        Deposit -> 1
        Withdraw -> 2
        Transfer -> 3
            
            Enter your choice >> ''')
    if select == '1':
        amount = input("Enter Amount (IRR): ")
        account.deposite(amount, auth_code)
    elif select == '2':
        amount = input("Enter Amount (IRR): ")
        account.withdraw(amount, auth_code)
    elif select == '3':
        pass
    else:
        print("Your choice is not valid!")
    return True