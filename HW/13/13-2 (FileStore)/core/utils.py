from core.models import DBModel
from users.models import User
from file.models import File
from configs import LOGGING_SETUP
from os import name as os_name, system as terminal
import logging
import psycopg2
from configs import DB_CONNECTION

def clear():
    terminal('cls' if os_name.lower() == 'nt' else 'clear')


class Logging:
    log_format = LOGGING_SETUP["log_format"]
    filename = LOGGING_SETUP["filename"]
    filemode = LOGGING_SETUP["filemode"]
    level = LOGGING_SETUP["level"]
    
    log_levels = {
        'debug': logging.DEBUG,
        'info': logging.INFO,
        'warning': logging.WARNING,
        'error': logging.ERROR,
        'critical': logging.CRITICAL
    }
    
    logging.basicConfig(filename, filemode, level, log_format)
    
    def __init__(self, log_level="Debug", log_message="defualt message"):
        self.log_level = log_level
        self.log_message = log_message
        
    @property
    def log_level(self):
        return self._log_level
    
    @log_level.setter
    def log_level(self, level: str):
        if level.lower() in Logging.log_levels:
            self._log_level = level
        logging.log(Logging.log_levels['error'], f"The Log_level of {level} is wrong.")
        
    def LOG(log_level, log_message) -> None:
        logging.log(log_level, log_message)

        
def create_tables() -> None:
    """ create tables in the PostgreSQL database"""
    commands = (
        """ CREATE TABLE IF NOT EXISTS users (
                user_id SERIAL PRIMARY KEY,
                first_name VARCHAR(50) NOT NULL,
                last_name VARCHAR(50) NOT NULL,
                phone VARCHAR(13) NOT NULL,
                national_code VARCHAR(10) NOT NULL,
                age integer NOT NULL,
                password VARCHAR(255) NOT NULL,
                is_seller BOOLEAN NOT NULL
                )
        """,
        """
        other: str, id: int=None
        CREATE TABLE IF NOT EXISTS files (
                file_id SERIAL PRIMARY KEY,
                file_name VARCHAR(255) NOT NULL,
                date_created DATE NOT NULL,
                date_modified DATE NOT NULL,
                seller_id INTEGER NOT NULL,
                FOREIGN KEY (seller_id)
                    REFERENCES User (user_id)
                    ON UPDATE CASCADE ON DELETE CASCADE,
                other VARCHAR(255),
        )
        """)
    try:
        DBname = DB_CONNECTION["DBname"]
        HOST = DB_CONNECTION["HOST"]
        USER = DB_CONNECTION["USER"]
        PORT = DB_CONNECTION["PORT"]
        PASSWORD = DB_CONNECTION["PASSWORD"]
        conn = psycopg2.connect(DBname, USER, HOST, PORT, PASSWORD)
        cur = conn.cursor()
        for command in commands: # Create tables one by one
            cur.execute(command)
        cur.close() # Close communication with the PostgreSQL database server
        conn.commit() # Commit the changes
    except (Exception, psycopg2.DatabaseError) as error:
        Logging.LOG('error', error)
    finally:
        logging.log('info', "users and files tables created in DB.")
        if conn is not None:
            conn.close()
            
def generate_command(model_instance: DBModel, method: str) -> str:
    
    values_args = {
            "user": 7,
            "file": 5
        }
    returning = ""
    if model_instance.id is None:
        id_sentence = ""
        returning = "RETURNING "+model_instance.TABLE[:-1]+"_id"
    else:
        id_sentence = model_instance.TABLE[:-1]+"_id" # == user_id or file_id
        values_args[model_instance.TABLE[:-1]] += 1
        
    if method.lower() == "insert":

        if isinstance(model_instance, User):
            command = "users("+id_sentence+"first_name, last_name, phone, national_code, age, password, is_seller) "   
        else:
            command = "files("+id_sentence+"file_name, date_created, date_modified, seller_id, other) "
        
        command += "VALUES( %s"+(", %s")*(values_args[model_instance.TABLE[:-1]]-1)+") "+returning
        
    elif method.lower() == "get":
        command = "SELECT * FROM "+model_instance.TABLE[:-1]+" WHERE "+id_sentence+" = %s"
    
    elif method.lower() == "update":
        command = "UPDATE "+model_instance.TABLE[:-1]
        if isinstance(model_instance, User):
            command += " SET first_name = %s,last_name = %s, phone = %s, national_code = %s, age = %s, password = %s, is_seller = %s"   
        else:
            command += " SET file_name = %s, date_created = %s, date_modified = %s, seller_id = %s, other = %s"
        command += " WHERE "+id_sentence+" = %s"
    
    elif method.lower() == "delete":
        command = "DELETE FROM "+model_instance.TABLE[:-1]+" WHERE "+id_sentence+ "= %s"
        
    return command
    