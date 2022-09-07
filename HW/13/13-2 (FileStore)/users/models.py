from core.models import DBModel
import logging.config, logging
import re

# Define Logger:
logging.config.fileConfig('.\\log_configs.ini', disable_existing_loggers=False)
logger = logging.getLogger(__name__)

class User(DBModel):  # User model
    TABLE = 'users'
    PK = 'id'

    def __init__(self, first_name, last_name, phone, national_id, age: int, password, is_seller: bool=False, id: int=None) -> None:

        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.national_id = national_id
        self.age = age
        self.password = password
        self.is_seller = is_seller
        self.id = id
        
    @property
    def first_name(self):
        return self._first_name
    
    @first_name.setter
    def first_name(self, first_name):
        if User.name_validation(first_name):
            self._first_name = first_name
        else:
            logger.error("First Name is not valid.")
    
    @property
    def last_name(self):
        return self._last_name
    
    @last_name.setter
    def last_name(self, last_name):
        if User.name_validation(last_name):
            self._last_name = last_name
        else:
            logger.error("Last Name is not valid.")
            
    @classmethod
    def name_validation(cls, name):
        match_name = re.fullmatch(r'[a-zA-Z]{4,14}',name)
        if match_name is None:
            return False
        return True
    
    @property
    def phone(self):
        return self._phone
    
    @phone.setter
    def phone(self, phone):
        if User.phone_validation(phone):
            self._phone = phone
        else:
            logger.error("Phone Number is not valid.")
        
    @classmethod
    def phone_validation(cls, phone):
        pattern = '(\A09+[0-9]{9})|(\A\+989+[0-9]{9})'
        match_phone = re.fullmatch(pattern, phone)
        if match_phone is None:
            return False
        return True
    
    @property
    def national_id(self):
        return self._national_id
    
    @national_id.setter
    def national_id(self, national_id):
        if User.national_id_validation(national_id):
            self._national_id = national_id
        else:
            logger.error("National ID is not valid.")
        
    @classmethod
    def national_id_validation(cls, national_id):
        pattern = r'([0-9]{10})'
        match_national_id = re.fullmatch(pattern, national_id)
        if match_national_id is None:
            return False
        return True
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, age):
        if User.age_validation(age):
            self._age = age
        else:
            logger.error("Age must be an integer between 01-99.")
        
    @classmethod
    def age_validation(cls, age):
        pattern = '^0*(?:[1-9][0-9]?|100)$'
        match_age = re.fullmatch(pattern, str(age))
        if match_age is None:
            return False
        return True
    
    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, id):
        if id is not None:
            if User.id_validation(id):
                self._id = id
            else:
                logger.error("user_id must be an integer more than 0. user_id set to None.")
                self._id = None
        else:
            self._id = None
        
    @classmethod
    def id_validation(cls, id):
        if id <= 0:
            return False
        return True


