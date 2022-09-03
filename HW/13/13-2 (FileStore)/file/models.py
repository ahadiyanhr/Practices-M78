from core.models import DBModel
from core.utils import Logging
import re


class File(DBModel):  # User model
    TABLE = 'files'
    PK = 'id'

    def __init__(self, file_name, date_created, date_modified, seller, other, id: int=None) -> None:

        self.file_name = file_name
        self.date_created = date_created
        self.date_modified = date_modified
        self.seller = seller
        self.other = other
        if id: self.id = id