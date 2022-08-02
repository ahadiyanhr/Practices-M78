from User import User
from admin import Admin

#User:
    # create a user only by program interface???
    # must have a private_unique_id that produce by program and show it when a user create
    # ... works as Authentication id to have a trip or use bank account

#Admins:
    # only admins can control the program
    # must have a private_unique_id that produce by program and show it when a user create
    # ... works as Authentication id to have a trip or use bank account

test_admin = Admin("Saeed", "Rezaei", "0155554781", "myPass123", "09122224444")


if __name__ == "__main1__":
    
    loop = True
    choice = ''
    print("\n-----------\nHi dear, Welcome to my Program, :)")
    while loop:
        choice = input('''\nPlease select your option:
            Quit -> 0
            Sign Up -> 1
            Log in -> 2
            
                Enter your choice >> ''')
        
        #----- User select "0" from Main Menu:
        if choice == '0':
            print("Quit from Menu")
            break
        
        #----- User select "1" from Main Menu:
        elif choice == '1':
            print("\n----> Sign Up Menu <----")
            get_username = input('Enter Your Username: ')
            get_password = input('Enter Your Password: ')
            get_phone = input('Do you have Phone Number? y/N ')
            
            if get_phone in ['', 'n', 'N']:
                phone_number = None
            else:
                phone_number = input('Enter Your Phone Number: ')
            
            User.sign_up(get_username, get_password, phone_number)
        
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
    