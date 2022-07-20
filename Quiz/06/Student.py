class Student:
    
    def __init__(self, first_name: str, last_name: str, age: int, phone_number: str, email: str):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.phone_number = phone_number
        self.email = email
        
    def data(self):
        data_dict = {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age,
            'email': self.email
        }
        return data_dict


class Student2:
    
    def __init__(self, first_name: str, last_name: str, age: int, phone_number: str, email: str , **kwargs):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.phone_number = phone_number
        self.email = email
        self.kwargs = kwargs
        
    def data(self):
        data_dict = {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age,
            'email': self.email
        }
        data_dict.update(self.kwargs)

        return data_dict