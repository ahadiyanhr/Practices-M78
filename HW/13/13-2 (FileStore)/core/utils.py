from core.models import DBModel
from users.models import User
from file.models import File
from os import name as os_name, system as terminal
import logging.config, logging
import psycopg2
from configs import DB_CONNECTION

# Define Logger:
logging.config.fileConfig('.\\log_configs.ini', disable_existing_loggers=False)
logger = logging.getLogger(__name__)

def clear():
    terminal('cls' if os_name.lower() == 'nt' else 'clear')
        
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
        CREATE TABLE IF NOT EXISTS files (
                file_id SERIAL PRIMARY KEY,
                file_name VARCHAR(255) NOT NULL,
                date_created DATE NOT NULL,
                date_modified DATE NOT NULL,
                seller_id INTEGER NOT NULL,
                FOREIGN KEY (seller_id)
                    REFERENCES users (user_id)
                    ON UPDATE CASCADE ON DELETE CASCADE,
                other VARCHAR(255)
        )
        """)
    try:
        DBname = DB_CONNECTION["DBname"]
        USER = DB_CONNECTION["USER"]
        PASSWORD = DB_CONNECTION["PASSWORD"]
        conn = psycopg2.connect(dbname=DBname, user=USER, password=PASSWORD)
        cur = conn.cursor()
        for command in commands: # Create tables one by one
            cur.execute(command)
        cur.close() # Close communication with the PostgreSQL database server
        conn.commit() # Commit the changes
    except (Exception, psycopg2.DatabaseError) as error:
        logger.error(error)
    finally:
        logger.info("users and files tables created in DB.")
        if conn is not None:
            conn.close()
            
def generate_command(model_instance: DBModel, method: str) -> str:
    
    values_args = {
            "user": 7,
            "file": 5
        }
    returning = ""
    if not isinstance(model_instance.id, int):
        id_sentence = ""
        returning = "RETURNING "+model_instance.TABLE[:-1]+"_id"
    else:
        id_sentence = model_instance.TABLE[:-1]+"_id" # == user_id or file_id
        values_args[model_instance.TABLE[:-1]] += 1
        
    if method.lower() == "insert":

        if isinstance(model_instance, User):
            command = "INSERT INTO users("+id_sentence+"first_name, last_name, phone, national_code, age, password, is_seller) "   
        else:
            command = "INSERT INTO files("+id_sentence+"file_name, date_created, date_modified, seller_id, other) "
        
        command += "VALUES( %s"+(", %s")*(values_args[model_instance.TABLE[:-1]]-1)+") "+returning
    
    elif method.lower() == "update":
        command = "UPDATE "+model_instance.TABLE
        if isinstance(model_instance, User):
            command += " SET first_name = %s,last_name = %s, phone = %s, national_code = %s, age = %s, password = %s, is_seller = %s"   
        else:
            command += " SET file_name = %s, date_created = %s, date_modified = %s, seller_id = %s, other = %s"
        command += " WHERE "+id_sentence+" = %s"
        
    return command

def print_attrs(fetch_data: dict, attribute="all") -> (dict|str):
    try:
        if attribute.lower() == "all":
            return fetch_data
        else:
            return fetch_data[attribute]
    except Exception as error:
            logger.error(error)