import os
import exceptions as ex 
from User import User
from Admin import Admin
from BankAccount import BankAccount
from MetroCard import CreditCard, LimitedCard, SingleCard



    # create trip (origin, destination, Fare)
    # each trip can do by one until end


    # 1. user register ==> pickle it, show Authentication id
    # 2. bank account management ==> with Authentication id
    # 3. record a trip to a dict (key: trip_number, value: info): get A_id, select MetroCard (ask about charge it?), Pay for ticket and record it
    # 4. Management: get Admin_id and password, go to admin control:
    #   record a metro trip
    #   edit a trip that has already been made 

if __name__ == "__main__":
    
    loop = True
    choice = ''
    print("\n-----------\nHi dear, Welcome to my Metro Program, :)")
    while loop:
        choice = input('''\nPlease select your option:
            Quit -> 0
            User/Admin Register -> 1
            Bank Account Management -> 2
            Take a Trip -> 3
            Trip Managment (by admin) -> 4
            
                Enter your choice >> ''')
        
        #----- User select "0" from Main Menu:
        if choice == '0':
            os.system("cls")
            print("Quit from Menu")
            break
        
        #----- User select "1" from Main Menu:
        elif choice == '1':
            os.system("cls")
            print("\n----> Register Menu <----")
            get_type = input('Enter Type of User (user/admin): ')
            get_first_name = input('Enter first_name: ')
            get_last_name = input('Enter last_name: ')
            get_id_number = input('Enter id_number (must be 10 numbers): ')
            get_password = input('Enter Password (must be more than 4 chars): ')
            get_phone = input('Do you have Phone Number? y/N ')
            
            if get_phone in ['', 'n', 'N']:
                phone_number = None
            else:
                phone_number = input('Enter Phone Number: ')
            
            if get_type == 'user':
                user = User(get_first_name, get_last_name, get_id_number, get_password, phone_number)
                print(f"User Authentication Code is {user.auth_code}")
            else:
                admin = Admin(get_first_name, get_last_name, get_id_number, get_password, phone_number)
                print(f"Admin Authentication Code is {admin.auth_code}")
            input('press enter to continue')
            os.system("cls") 
            continue
        
        #----- User select "2" from Main Menu:    
        elif choice == '2':
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
    