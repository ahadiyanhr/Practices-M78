import re

class User:
    def __init__(self, name: str, email: str, phone: str):
        self.name = name
        self.email = email
        self.phone = phone

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if User.name_validation(name):
            self._name = name
        else:
            raise ValueError("Name can include only alphabets and underscore.")
            
    @classmethod
    def name_validation(cls, name):
        match_name = re.findall('[a-zA-Z_]',name)
        if len(match_name) == len(name):
            return True
        return False
    
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, email):
        if User.email_validation(email):
            self._email = email
        else:
            raise ValueError("Email is not valid.")

    @classmethod
    def email_validation(cls, email):
        pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        match_email = re.fullmatch(pattern,email)
        if match_email is None:
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
            raise ValueError("PhoneNumber is not valid.")
        
    @classmethod
    def phone_validation(cls, phone):
        pattern = '(\A09+[0-9]{9})|(\A\+989+[0-9]{9})'
        match_phone = re.fullmatch(pattern,phone)
        if match_phone is None:
            return False
        return True
    
user1 = User('hamid_', 'ads@fasdsdfsd.ci', '+989120720171')