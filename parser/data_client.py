from abc import ABC, abstractmethod
from sqlite3 import Error
import psycopg2


class DataClient(ABC):
    @abstractmethod
    def get_connection(self):
        pass

    @abstractmethod
    def get_items(self, conn, table_name):
        pass

    @abstractmethod
    def create_table(self, conn, table_name):
        pass

    @abstractmethod
    def insert(self, conn, table_name, link, title, description, price):
        pass


class PostgresClient(DataClient):
    USER = "postgres"
    PASSWORD = "postgres"
    HOST = "localhost"
    PORT = "5432"

    def get_connection(self):
        try:
            connection = psycopg2.connect(
                dbname="flowers_shop",
                user=self.USER,
                password=self.PASSWORD,
                host=self.HOST,
                port=self.PORT
            )
            return connection
        except Error:
            print(Error)

    def create_table(self, conn, table_name):
        cursor_object = conn.cursor()
        cursor_object.execute(
            f"""
                CREATE TABLE IF NOT EXISTS {table_name}
                (
                    id serial PRIMARY KEY, 
                    link text, 
                    title text,
                    description text,
                    price numeric 
                )
            """
        )
        conn.commit()

    def get_items(self, conn, table_name):
        cursor = conn.cursor()
        cursor.execute(f'SELECT * FROM {table_name}')
        return cursor.fetchall()

    def insert(self, conn, table_name, link, title, description, price):
        cursor = conn.cursor()
        cursor.execute(
            f"INSERT INTO {table_name} (link, title, description, price) VALUES ('{link}', '{title}', '{description}', "
            f"'{price}')")
        conn.commit()

