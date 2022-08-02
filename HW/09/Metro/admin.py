import logging
import pickle
import exceptions as ex
import uuid

from User import User

class Admin(User):
    admins = []
    
    def __new__(cls, *args):
        for admin in Admin.admins:
            # Check the user with National ID Number already exists or not:
            if args[2] == admin.id_number:
                logging.log(logging.INFO, "This admin was already registered and can not created.")
                raise ex.InstantiateError("This admin was already registered.")
        return super(Admin, cls).__new__(cls, *args)
    
    def __init__(self, first_name: str, last_name: str, id_number: str, password: str, phone_number: str = None):
        super(Admin, self).__init__(first_name, last_name, id_number, password, phone_number)
        self.auth_code = str(uuid.uuid3(uuid.NAMESPACE_DNS, self.id_number)).split("-")[0] # make an Auth.Code
        Admin.admins.append(self) # add to admins list
        with open('admins.pickle', 'wb') as ap:
            pickle.dump(Admin.admins, ap)
        logging.log(logging.INFO, f"The admin created with Auth_ID of {self.auth_code} and pickled to admins.pickle file.")
            
        
    def __str__(self) -> str:
        return f"Authentication ID: {self.auth_code}"
    