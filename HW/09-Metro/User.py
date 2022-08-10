import logging
import pickle
from types import NoneType
import exceptions as ex
import uuid

# Logging Setup:
log_format = "%(asctime)s %(name)s %(levelname)s: %(message)s"
logging.basicConfig(filename= 'metro.log', filemode= 'a',\
    level= logging.DEBUG, format= log_format)

class User:
    users = []
    
    def __new__(cls, *args):
        for user in User.users:
            # Check the user with National ID Number already exists or not:
            if args[2] == user.id_number:
                logging.log(logging.INFO, "This user was already registered and can not created.")
                raise ex.InstantiateError("This user was already registered.")
        return super(User, cls).__new__(cls)
    
    def __init__(self, first_name: str, last_name: str, id_number: str, password: str, phone_number: str = None, is_admin: bool = False):
        self.first_name = first_name
        self.last_name = last_name
        self.id_number = id_number
        self.password = password
        self.phone_number = phone_number
        self.is_admin = is_admin
        self.auth_code = str(uuid.uuid3(uuid.NAMESPACE_DNS, self.id_number)).split("-")[0] # make an Auth.Code
        User.users.append(self) # add to users list
        with open('users.pickle', 'wb') as up:
            pickle.dump(User.users, up)
        logging.log(logging.INFO, f"The user created with Auth_ID of {self.auth_code} and pickled to users.pickle file.")
            
        
    def __str__(self) -> str:
        return f"Authentication Code: {self.auth_code}"
    
    @property
    def id_number(self):
        return self.__id_number
    
    @id_number.setter
    def id_number(self, id_number: str):
        if len(id_number) != 10:
            logging.log(logging.ERROR, f"The National ID Number was not equal to 10 characters.")
            raise ex.IDNumberError("The National ID Number must equal to 10 characters.")    
        self.__id_number = id_number
      
    @property
    def password(self):
        return self.__password
    
    @password.setter
    def password(self, password: str):
        if len(password) < 4:
            logging.log(logging.ERROR, f"The password was not more than 3 characters.")
            raise ex.PasswordError("The password must be at least 4 characters.")    
        self.__password = password
        
    @property
    def phone_number(self):
        return self._phone_number
    
    @phone_number.setter
    def phone_number(self, phone_number: str):
        if not isinstance(phone_number, NoneType):
            if len(phone_number) != 11:
                logging.log(logging.ERROR, f"Phone Number was not equal to 11 characters.")
                raise ex.PhoneError("Phone Number must be 11 characters.")    
            elif phone_number[:2] != '09':
                logging.log(logging.ERROR, f"Phone Number did not start with \"09\".")
                raise ex.PhoneError("Phone Number must start with \"09\".")
        self._phone_number = phone_number

    
if __name__ == "__main__":
    
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

    

        

        
        