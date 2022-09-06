import psycopg2
import psycopg2.extras
from core.models import DBModel
from users.models import User
from configs import DB_CONNECTION
from psycopg2._psycopg import connection, cursor


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

    def create(self, model_instance: DBModel) -> int:
        """
            return id of created model instance from table
        """
        command_no_id = """
            INSERT INTO User(first_name, last_name, phone, national_code, age, password, is_seller) 
            VALUES(%s, %s, %s, %s , %s, %s, %s)
            RETURNING user_id
            """
        command_with_id = """
            INSERT INTO User(user_id, first_name, last_name, phone, national_code, age, password, is_seller) 
            VALUES(%s, %s, %s, %s, %s , %s, %s, %s)
            """
        if model_instance.id is None:
            self.__get_cursor().execute(command_no_id,\
                (model_instance.first_name, model_instance.last_name, phone, national_code, age, password, is_seller))
            row = cur.fetchone()
            self.id = row[0]
            cur.close()
            # commit the changes
            conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()

    def read(self, model_class: type, pk) -> DBModel:  # get
        """
            returns an instance of the Model with inserted values
        """

    def update(self, model_instance: DBModel) -> None:
        """
            update instance in db table by get all model_instance attrs
        """

    def delete(self, model_instance: DBModel) -> None:
        """
            delete instance method
        """
