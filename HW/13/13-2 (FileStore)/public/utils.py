import sys
sys.path.append('.\\')

from configs import INFO as information
from configs import Questions
from users import models as usmdl
from file import models as flmdl
from core import managers as mng
from core.utils import create_tables



def about_us():
    print(
        f"""Store name : {information["name"]}
Description : {information["description"]}
Version : {information["version"]}
"""
    )

def insert_to_table(model_class: str):
    create_tables()
    data = []
    i = 0
    for args in Questions[model_class.lower()]:
        data.append(input(args+" ("+Questions[model_class.lower()][args]+") :"))
        i += 1
    if model_class.lower() == 'user':
        u1 = usmdl.User(data[0], data[1], data[2], data[3], data[4], data[5], data[6])
    else:
        u1 = flmdl.File(data[0], data[1], data[2], data[3], data[4])
    db_manager = mng.DBManager()
    instance_id = db_manager.create(u1)
    print(f"A {model_class} with ID of {instance_id} created in its table.")
    
def read_from_table(model_class: str):
    db_manager = mng.DBManager()
    id = input(f"Enter ID of {model_class}: ")
    if model_class.lower() == 'user': 
        instance = db_manager.read(usmdl.User, id)
    else:
        instance = db_manager.read(flmdl.File, id)
    print(f"The instance read from {model_class} table with these information:\n {vars(instance)}")
    
def update_in_table(model_class: str):
    db_manager = mng.DBManager()
    id = int(input(f"Enter ID of {model_class}: "))
    data = []
    i = 0
    for args in Questions[model_class.lower()]:
        data.append(input(args+" ("+Questions[model_class.lower()][args]+") :"))
        i += 1
    if model_class.lower() == 'user': 
        old_instance = db_manager.read(usmdl.User, id)
    else:
        old_instance = db_manager.read(flmdl.File, id)
    print(f"The old instance from {model_class} table with these information:\n {vars(old_instance)}")
    
    if model_class.lower() == 'user':
        new_instance = usmdl.User(data[0], data[1], data[2], data[3], data[4], data[5], data[6], id)
    else:
        new_instance = flmdl.File(data[0], data[1], data[2], data[3], data[4], id)
    db_manager.update(new_instance)
    print(f"Updated to:\n {vars(new_instance)}")
    
def delete_from_table(model_class: str):
    db_manager = mng.DBManager()
    id = int(input(f"Enter ID of {model_class}: "))  
    if model_class.lower() == 'user': 
        instance = db_manager.read(usmdl.User, id)
    else:
        instance = db_manager.read(flmdl.File, id)
    db_manager.delete(instance)
    print(f"The instance is deleted from {model_class} table. the information was:\n {vars(instance)}")
