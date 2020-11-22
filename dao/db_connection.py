import psycopg2
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dao.credentials import *

class PostgreDb(object):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = object.__new__(cls)
            try:
                connection = psycopg2.connect(user=username,
                                        password=password,
                                        host=host,
                                        port=port,
                                        database=database)
                cursor = connection.cursor()
                query = "select version();"
                cursor.execute(query)
                db_version = cursor.fetchone()
                print("New connection to {} created".format(db_version[0]))

                engine = create_engine(
                    f'postgresql://{username}:{password}@{host}:{port}/{database}',
                    pool_pre_ping=True
                )
                Session = sessionmaker(bind=engine)
                session = Session()
                PostgreDb._instance.connection = connection
                PostgreDb._instance.cursor = cursor
                PostgreDb._instance.sqlalchemy_session = session
                PostgreDb._instance.sqlalchemy_engine = engine
            except Exception as error:
                print('Error: connection not established {}'.format(error))
        else:
            print('Connection already established')

        return cls._instance

    def __init__(self):
        self.connection = self._instance.connection
        self.cursor = self._instance.cursor
        self.sqlalchemy_session = self._instance.sqlalchemy_session
        self.sqlalchemy_engine = self._instance.sqlalchemy_engine

    def execute(self, query):
        try:
            result = self.cursor.execute(query)
        except Exception as error:
            print('error execting query "{}", error: {}'.format(query, error))
            return None
        else:
            return result

    def __del__(self):
        self.cursor.close()
        self.connection.close()
        self.sqlalchemy_session.close()


if __name__ == "__main__":
    db = PostgreDb()
    db = PostgreDb()
    db = PostgreDb()
    db = PostgreDb()