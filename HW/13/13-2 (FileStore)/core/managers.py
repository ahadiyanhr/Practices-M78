import psycopg2
import psycopg2.extras
import logging.config, logging
from core.models import DBModel
from users import models as usmdl
from file import models as flmdl
from core.utils import generate_command
from configs import DB_CONNECTION
from psycopg2._psycopg import connection, cursor


# Define Logger:
logging.config.fileConfig('.\\log_configs.ini', disable_existing_loggers=False)
logger = logging.getLogger(__name__)

class DBManager:
    DBname = DB_CONNECTION["DBname"]
    HOST = DB_CONNECTION["HOST"]
    USER = DB_CONNECTION["USER"]
    PORT = DB_CONNECTION["PORT"]
    PASSWORD = DB_CONNECTION["PASSWORD"]

    def __init__(self, dbname=DBname, user=USER, host=HOST, port=PORT, password=PASSWORD) -> None:
        self.dbname = dbname
        self.user = user
        self.host = host
        self.port = port
        self.password = password

        self.conn: connection = \
            psycopg2.connect(dbname=self.dbname, user=self.user, host=self.host, port=self.port, password=password)

    def __del__(self):
        self.conn.close()  # Close the connection on delete

    def __get_cursor(self) -> cursor:
        # Changing the fetch output from Tuple to Dict utilizing RealDictCursor cursor factory
        return self.conn.cursor()#(cursor_factory=psycopg2.extras.RealDictCursor)
    
    def __close_cursor(self) -> None:
        return self.conn.cursor().close()
    
    def __get_execute(self, model_instance: DBModel, method: str) -> (tuple|None):
        
        command = generate_command(model_instance, method)
        cur = self.__get_cursor()

        if (method == "insert") and (model_instance.id is None):
            if isinstance(model_instance, usmdl.User):
                cur.execute(command, (model_instance.first_name, model_instance.last_name,\
                    model_instance.phone, model_instance.national_id, model_instance.age,\
                        model_instance.password, model_instance.is_seller))
                logger.info(f"User instance with name of {model_instance.first_name} inserted into {usmdl.User.TABLE} table.")
            else:
                cur.execute(command, (model_instance.file_name, model_instance.date_created,\
                    model_instance.date_modified, model_instance.seller_id, model_instance.other))
                logger.info(f"File instance with name of {model_instance.file_name} inserted into {flmdl.File.TABLE} table.")
            return cur.fetchone()
        
        elif method == "insert":
            if isinstance(model_instance, usmdl.User):
                cur.execute(command, (model_instance.id, model_instance.first_name, model_instance.last_name,\
                    model_instance.phone, model_instance.national_id, model_instance.age, model_instance.password, model_instance.is_seller))
                logger.info(f"User instance with id of {model_instance.id} inserted into {usmdl.User.TABLE} table.")
            else:
                cur.execute(command, (model_instance.id, model_instance.file_name, model_instance.date_created,\
                    model_instance.date_modified, model_instance.seller_id, model_instance.other))
                logger.info(f"File instance with id of {model_instance.id} inserted into {flmdl.File.TABLE} table.")
            return cur.fetchone()
        
        elif method == "update":
            if isinstance(model_instance, usmdl.User):
                cur.execute(command, (model_instance.first_name, model_instance.last_name, model_instance.phone,\
                    model_instance.national_id, model_instance.age, model_instance.password, model_instance.is_seller, model_instance.id))
                logger.info(f"User instance with id of {model_instance.id} updated in {usmdl.User.TABLE} table.")
            else:
                cur.execute(command, (model_instance.file_name, model_instance.date_created,\
                    model_instance.date_modified, model_instance.seller_id, model_instance.other, model_instance.id))
                logger.info(f"File instance with id of {model_instance.id} updated in {flmdl.File.TABLE} table.")

    def create(self, model_instance: DBModel) -> int:
        """
            return id of created model instance from table
        """
        try:
            row = self.__get_execute(model_instance, "insert")
            model_instance.id = row[0] # get id of instance
            self.__close_cursor() # close cursor
            self.conn.commit() # commit the changes
        except (Exception, psycopg2.DatabaseError) as error:
            logger.error(error)
        finally:
            if self.conn is not None:
                self.__del__()
        return model_instance.id

    def read(self, model_class: type, id: int) -> DBModel:
        """
            returns an instance of the Model with inserted values
        """
        command = "SELECT * FROM "+model_class.TABLE+" WHERE "+model_class.TABLE[:-1]+"_id = %s"
        try:
            cur = self.__get_cursor()
            cur.execute(command, (id,))
            data = cur.fetchall()
            self.__close_cursor() # close cursor
            self.conn.commit() # commit the changes
            if model_class.TABLE == "users":
                instance = usmdl.User(data[0][1], data[0][2], data[0][3], data[0][4], data[0][5], data[0][6], data[0][7], data[0][0])
                logger.info(f"User instance with id of {data[0][0]} get from {model_class.TABLE} table.")
            else:
                instance = flmdl.File(data[0][1], data[0][2], data[0][3], data[0][4], data[0][5], data[0][0])
                logger.info(f"User instance with id of {data[0][0]} get from {model_class.TABLE} table.")
            return instance
        except (Exception, psycopg2.DatabaseError) as error:
            logger.error(error)
            raise(Exception)
        finally:
            if self.conn is not None:
                self.__del__()

    def update(self, model_instance: DBModel) -> None:
        """
            update instance in db table by get all model_instance attrs
        """
        try:
            self.__get_execute(model_instance, "update")
            self.__close_cursor() # close cursor
            self.conn.commit() # commit the changes
        except (Exception, psycopg2.DatabaseError) as error:
            logger.error(error)
        finally:
            if self.conn is not None:
                self.__del__()

    def delete(self, model_instance: DBModel) -> None:
        """
            delete instance method
        """
        command = "DELETE FROM "+model_instance.TABLE+" WHERE "+model_instance.TABLE[:-1]+"_id = %s"
        try:
            cur = self.__get_cursor()
            cur.execute(command, (model_instance.id,))
            logger.info(f"{model_instance.TABLE[:-1]} instance with id of {model_instance.id} remove from {model_instance.TABLE} table.")
            self.__close_cursor() # close cursor
            self.conn.commit() # commit the changes
        except (Exception, psycopg2.DatabaseError) as error:
            logger.error(error)
        finally:
            if self.conn is not None:
                self.__del__()
