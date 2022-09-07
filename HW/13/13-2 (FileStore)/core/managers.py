import psycopg2
import psycopg2.extras
import logging.config, logging
from core.models import DBModel
from users.models import User
from file.models import File
from core.utils import generate_command, print_attrs
from configs import DB_CONNECTION
from psycopg2._psycopg import connection, cursor


# Define Logger:
logging.config.fileConfig('.\\log_configs.ini', disable_existing_loggers=False)
logger = logging.getLogger(__name__)

class DBManager:
    HOST = DB_CONNECTION["HOST"]
    USER = DB_CONNECTION["USER"]
    PORT = DB_CONNECTION["PORT"]
    PASSWORD = DB_CONNECTION["PASSWORD"]

    def __init__(self, database, user=USER, host=HOST, port=PORT, password=PASSWORD) -> None:
        self.database = database
        self.user = user
        self.host = host
        self.port = port
        self.password = password

        self.conn: connection = \
            psycopg2.connect(dbname=self.database, user=self.user, host=self.host, port=self.port, password=password)

    def __del__(self):
        self.conn.close()  # Close the connection on delete

    def __get_cursor(self) -> cursor:
        # Changing the fetch output from Tuple to Dict utilizing RealDictCursor cursor factory
        return self.conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    
    def __close_cursor(self) -> None:
        return self.conn.cursor().close()
    
    def __get_execute(self, model_instance: DBModel, method: str) -> cursor:
        command = generate_command(model_instance, method)
        
        if (method == "insert") and (model_instance.id is None):
            if isinstance(model_instance, User):
                return self.__get_cursor().execute(command, (model_instance.first_name, model_instance.last_name,\
                    model_instance.phone, model_instance.national_code, model_instance.age, model_instance.password, model_instance.is_seller))
            else:
                return self.__get_cursor().execute(command, (model_instance.file_name, model_instance.date_created,\
                    model_instance.date_modified, model_instance.seller_id, model_instance.other))
        
        elif method == "insert":
            if isinstance(model_instance, User):
                return self.__get_cursor().execute(command, (model_instance.id, model_instance.first_name, model_instance.last_name,\
                    model_instance.phone, model_instance.national_code, model_instance.age, model_instance.password, model_instance.is_seller))
            else:
                return self.__get_cursor().execute(command, (model_instance.id, model_instance.file_name, model_instance.date_created,\
                    model_instance.date_modified, model_instance.seller_id, model_instance.other))
        
        elif method == "update":
            if isinstance(model_instance, User):
                return self.__get_cursor().execute(command, (model_instance.first_name, model_instance.last_name, model_instance.phone,\
                    model_instance.national_code, model_instance.age, model_instance.password, model_instance.is_seller, model_instance.id))
            else:
                return self.__get_cursor().execute(command, (model_instance.file_name, model_instance.date_created,\
                    model_instance.date_modified, model_instance.seller_id, model_instance.other, model_instance.id))

    def create(self, model_instance: DBModel) -> int:
        """
            return id of created model instance from table
        """
        try:
            row = self.__get_execute(model_instance, "insert").fetchone()
            self.id = row[0] # get id of instance
            self.__close_cursor() # close cursor
            self.conn.commit() # commit the changes
        except (Exception, psycopg2.DatabaseError) as error:
            logger.error(error)
        finally:
            if self.conn is not None:
                self.__del__()
        return self.id

    def read(self, model_class: type, id: int) -> DBModel:
        """
            returns an instance of the Model with inserted values
        """
        command = "SELECT * FROM "+model_class.TABLE+" WHERE "+model_class.TABLE[:-1]+"_id = %s"
        try:
            self.__get_cursor().execute(command, (id))
            data = self.__get_cursor().fetchall()
            attribute = input("Enter the attribute (all | any): ")
            print(print_attrs(data, attribute))
            self.__close_cursor() # close cursor
            self.conn.commit() # commit the changes
        except (Exception, psycopg2.DatabaseError) as error:
            Logging.LOG('error', error)
        finally:
            if self.conn is not None:
                self.__del__()

    def update(self, model_instance: DBModel) -> None:
        """
            update instance in db table by get all model_instance attrs
        """
        try:
            self.__get_execute(model_instance, "updata")
            self.__close_cursor() # close cursor
            self.conn.commit() # commit the changes
        except (Exception, psycopg2.DatabaseError) as error:
            Logging.LOG('error', error)
        finally:
            if self.conn is not None:
                self.__del__()

    def delete(self, model_class: type, id: int) -> None:
        """
            delete instance method
        """
        command = "DELETE FROM "+model_class.TABLE+" WHERE "+model_class.TABLE[:-1]+"_id = %s"
        try:
            self.__get_cursor().execute(command, (id))
            self.__close_cursor() # close cursor
            self.conn.commit() # commit the changes
        except (Exception, psycopg2.DatabaseError) as error:
            Logging.LOG('error', error)
        finally:
            if self.conn is not None:
                self.__del__()
