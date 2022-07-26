class Register:
    
    def __init__(self, first_name, last_name, age, phone_number, id, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.phone_number = phone_number
        self.id = id
        self.email = email
    
    def input_first_name(self, name):
        if  2 <= len(name) <= 120:
            self.first_name = name
    
    def input_last_name(self, name):
        if  2 <= len(name) <= 120:
            self.last_name = name
          
    def input_age(self, value):
        if  9 <= value <= 120:
            self.age = value
    
    def input_phone(self, value):
        if  len(value) == 9 and (value[:1] == '09'):
            self.phone_number = value
            
    def input_id(self, value):
        if  len(value) == 10:
            self.id = value
    
    def input_email(self, email):
        if  ('@' in email) and ('.' in email) and (email.find('@') < email.find('.')):
            self.email = email

        

