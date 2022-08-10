import os
import exceptions as ex 
from User import User
from Admin import Admin
from BankAccount import BankAccount
from MetroCard import MetroCard
from Trip import Trip
import other_func as func

 

    # create trip (origin, destination, Fare)
    # each trip can do by one until end
    
    # 2. bank account management ==> with Authentication id
    # 3. record a trip to a dict (key: trip_number, value: info): get A_id, select MetroCard (ask about charge it?), Pay for ticket and record it
    # 4. Management: get Admin_id and password, go to admin control:
    #   record a metro trip
    #   edit a trip that has already been made 

if __name__ == "__main__":
    os.system("cls")
    loop = True
    choice = ''
    print("\n-----------\nHi dear, Welcome to my Metro Program, :)")
    while loop:
        choice = input(func.main_menu)
        
        #----- User select "0.Quit" from Main Menu:
        if choice == '0':
            os.system("cls")
            print("Quit from Menu")
            break
        
        #----- User select "1.Register" from Main Menu:
        elif choice == '1':
            os.system("cls")
            print("\n----> Register Menu <----")
            get_type = input('Enter Type of User (user/admin): ')
            if get_type.lower() not in ["user", "admin"]:
                input('Input type is not valid.\npress enter to continue ')
                continue
            fn = input('Enter first_name: ')
            ln = input('Enter last_name: ')
            id = input('Enter id_number (must be 10 numbers): ')
            ps = input('Enter Password (must be more than 4 chars): ')
            phi = input('Do you have Phone Number? y/N ')
            if phi in ['', 'n', 'N']:
                ph = None
            else:
                ph = input('Enter Phone Number: ')
            if get_type == 'user':
                user = User(fn, ln, id, ps, ph)
                account = BankAccount(user)
                print(f"User Authentication Code is {user.auth_code}")
            else:
                admin = Admin(fn, ln, id, ps, ph)
                account = BankAccount(admin)
                print(f"Admin Authentication Code is {admin.auth_code}")
            input('press enter to continue ')
            continue
        
        #----- User select "2.AccountManage" from Main Menu:    
        elif choice == '2':
            os.system("cls")
            print("\n----> Account Management Menu <----")
            get_authcode = input('Enter Your Authentication Code: ')
            if func.search_auth_code(get_authcode):
                account = func.search_auth_code(get_authcode)
                os.system("cls")
                print('Sign in succesed.')
                acc_select = input(func.acc_manage)
                if acc_select == '1': # Select Bank Account Management
                    os.system("cls")
                    bnk_select = input(func.bank_acc_selection)
                    func.bank_account_manage(bnk_select, account, get_authcode)
                    input('Done.\npress enter to continue ')
                    os.system("cls")
                    continue 
                elif acc_select == '2': # Select Metro Card Management
                    os.system("cls")
                    card_select = input(func.card_selection)
                    os.system("cls")
                    method_select = input(func.card_func_selection)
                    func.metro_card_manage(card_select, method_select, account, get_authcode)
                    continue
                else:
                    input('Your choice is invalid.\npress enter to continue ')
                    continue   
            else:
                input('Authentication Code is wrong.\npress enter to continue ')
                os.system("cls")
                continue
        
        
        #----- User select "0.Quit" from Main Menu:
        if choice == '3':
            os.system("cls")
            print("Now you can take a Trip!")
            origin = input('Enter origin: ')
            destination = input('Enter destination: ')
            fare = int(input("Enter trip's fare: "))
            auth_code = input('Enter Authentication Code: ')
            select = int(input("select card: 1.Credit, 2.Limited, 3.Single: "))
            user = func.get_owner(auth_code)
            for card in MetroCard.owner_cards[user]:
                if card[1] == ["CreditCard","LimitedCard","SingleCard"][select-1]:
                    card[0].pay_ticket(fare, auth_code)
                    Trip.record_trip(origin, destination, fare, auth_code)
                    input(f'Trip number {len(Trip._trip_records)} is done. press enter to continue.')
            continue
            
            
            
        
    