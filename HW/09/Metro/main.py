import os
import exceptions as ex 
from User import User
from Admin import Admin
from BankAccount import BankAccount
from MetroCard import CreditCard, LimitedCard, SingleCard
import menu_func as func

 

    # create trip (origin, destination, Fare)
    # each trip can do by one until end
    
    # 1. user register ==> pickle it, show Authentication id
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
            info = func.register()
            if get_type == 'user':
                user = User(info[0], info[1], info[2], info[3], info[4])
                account = BankAccount(user)
                print(f"User Authentication Code is {user.auth_code}")
            else:
                admin = Admin(info[0], info[1], info[2], info[3], info[4])
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
                if acc_select == '1':
                    func.bank_account_manage(account, get_authcode)
                    input('Done.\npress enter to continue ')
                    continue 
                elif acc_select == '2':
                    card_select = input(func.card_func_selection)
                    pass
                else:
                    input('Your choice is invalid.\npress enter to continue ')
                    continue   
            else:
                input('Authentication Code is wrong.\npress enter to continue ')
                os.system("cls")
                continue
            
            
            
            
            
        #----- User select "200" from Main Menu:    
        elif choice == '10':
            print("\n----> Log in Menu <----")
            get_username = input('Enter Your Username: ')
            get_password = input('Enter Your Password: ')
            
            if isinstance(User.user_valid(get_username, get_password),str):
                print(f"{get_username} signed in successfully!")
                user_id = User.user_valid(get_username, get_password)
                menuloop = True
                
                while menuloop:
                    menu = input('''\nPlease select your option:
        Print User Information -> 1
        Modify your Information -> 2
        Change your Password -> 3
        Exit from User Menu -> 4
        
            Enter your choice >> ''')

                    #----- User select "1" from User Menu:
                    if menu == '1':
                        print(User.users[user_id])
                    
                    #----- User select "2" from User Menu:
                    elif menu == '2':
                        get_username = input('Enter Your Username: ')
                        if User.user_valid(get_username, None):
                            print(f"This username has been taken by others! Please take another one.")
                        
                        get_phone = input('Do you have Phone Number? y/N ')
                        if get_phone in ['', 'n', 'N']:
                            phone_number = None
                        else:
                            phone_number = input('Enter Your Phone Number: ')
                        
                        User.users[user_id].username = get_username
                        User.users[user_id].phone_number = phone_number
                        
                    #----- User select "3" from User Menu:    
                    elif menu == '3':
                        old_pass = input("Enter your old Password: ")
                        new_pass = input("Enter your new Password: ")
                        repeat_new = input("Repeat your new Password: ")
                        if (User.users[user_id].password == old_pass) and (User.pass_valid(new_pass, repeat_new)):
                                User.users[user_id].password = new_pass
                                print("Password Updated!\nPlese log in again with your new Password.")
                                menuloop = False
                        elif User.users[user_id].password == old_pass:
                            print("New passwords are not match!")
                        else:
                            print("Password is wrong!")
                            
                    #----- User select "4" from User Menu:    
                    elif menu == '4':
                        menuloop = False
                        
            elif User.user_valid(get_username, get_password):
                print("Password is wrong!")
            else:
                print("There is not any User!")
    