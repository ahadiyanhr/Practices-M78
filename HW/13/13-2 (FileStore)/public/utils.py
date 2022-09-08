import sys
sys.path.append('.\\')

from configs import INFO as information
from configs import USER
from users import models as usmdl
from core import managers as mng
from core.utils import create_tables



def about_us():
    print(
        f"""Store name : {information["name"]}
Description : {information["description"]}
Version : {information["version"]}
"""
    )

def insert_to_table():
    create_tables()
    data = []
    i = 0
    for args in USER:
        data.append(input(args+" ("+USER[args]+") :"))
        i += 1
    u1 = usmdl.User(data[0], data[1], data[2], data[3], data[4], data[5], data[6])
    db_manager = mng.DBManager()
    db_manager.create(u1)
    
        
def salam(name):
    print("Hello ", name)
