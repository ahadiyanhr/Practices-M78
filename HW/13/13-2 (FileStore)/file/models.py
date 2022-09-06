from core.models import DBModel
from core.utils import Logging
import re


class File(DBModel):  # File model
    TABLE = 'files'
    PK = 'id'
    FK = 'seller_id'

    def __init__(self, file_name, date_created, date_modified, seller_id, other="", id: int=None) -> None:

        self.file_name = file_name
        self.date_created = date_created
        self.date_modified = date_modified
        self.seller_id = seller_id
        self.other = other
        if id: self.id = id
    
    @property
    def date_created(self):
        return self._date_created
    
    @date_created.setter
    def date_created(self, date_created):
        if File.date_validation(date_created):
            self._date_created = date_created
        Logging.LOG('error', "Date Created is not valid.")
        
    @property
    def date_modified(self):
        return self._date_modified
    
    @date_modified.setter
    def date_modified(self, date_modified):
        if File.date_validation(date_modified):
            self._date_modified = date_modified
        Logging.LOG('error', "Date Modified is not valid.")
        
    @classmethod
    def date_validation(cls, date):
        pattern = r'^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])'
        match_date = re.fullmatch(pattern, date)
        if match_date is None:
            return False
        return True
    
    @property
    def seller_id(self):
        return self._seller_id
    
    @seller_id.setter
    def seller_id(self, seller_id):
        if File.seller_id_validation(seller_id):
            self._seller_id = seller_id
        Logging.LOG('error', f"There is no seller with id of {seller_id}.")
        
    @classmethod
    def seller_id_validation(cls, seller_id):
        '''not compeleted func. + unittest'''
        return NotImplemented