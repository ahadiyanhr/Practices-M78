import uuid

class User:
    users = {} 
    def __init__(self, username: str, phone_number: str = None):
        self.username = username
        self.__password = ''
        self.phone_number = phone_number
        # make a UUID using an MD5 hash of a namespace UUID and username:
        self.id = str(uuid.uuid3(uuid.NAMESPACE_DNS, username))
    
    def __str__(self):
        return f"-----------\nUsername: {self.username}\nUserID: {self.id}\nPhone Number: {self.phone_number}\n-----------"
    
    @property
    def password(self):
        return self.__password
    
    @password.setter
    def password(self, pass_string: str):
        if len(pass_string) < 4:
            raise ValueError("The password must be at least 4 char!")    
        self.__password = pass_string

    
    
    @staticmethod
    def sign_up(username: str, password: str, phone_number: str = None) -> str:
        '''
        This method sign up a new User
        '''       
        registered_user = User(username, phone_number)
        registered_user.password = password
        User.users[registered_user.id] = (registered_user)
        print(f"{registered_user.username} is signed up.\n")
        return registered_user
    

    @staticmethod
    def user_valid(username:str , password) -> str or True or False:
        '''
        This method validate an existing User by his/her username and password
        '''            
        for items in User.users.values():
            if (items.username == username) and (items.password == password):
                return items.id
            elif items.username == username:
                return True
        return False
    
    @staticmethod
    def pass_valid(new_pass, repeat_new):
        '''
        This method validate the new password that entered by User
        '''
        if new_pass == repeat_new:
            return True
        return False
        
    

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
    
        
        