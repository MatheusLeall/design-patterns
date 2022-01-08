import sqlite3
from typing import Any, Dict


class Singleton(type):
    __instances: Dict = {}

    def __call__(cls, *args: Any, **kwargs: Any) -> Any:
        if cls not in cls.__instances:
            cls.__instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls.__instances[cls]


class Database(metaclass=Singleton):

    connection = None

    def connect(self):
        if self.connection is None:
            print("Creating a new connection with the database...")
            self.connection = sqlite3.connect("new_database.sqlite3")
            self.cursor = self.connection.cursor()
        return self.cursor


db1 = Database().connect()

db2 = Database().connect()
