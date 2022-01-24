import sqlite3 as sql
from user import UserClass
from datetime import datetime
from operations.file_operations import FileOperations

class DBOperations():
    
    def __init__(self, db_name):
        self.db_name = db_name

    def connect(self):
        connection = sql.connect(self.db_name)
        return connection

    def updateTableName(self):
        return 'data_{}'.format(datetime.now().strftime("%d%m%Y"))

    def createTable(self):
        try:
            connectionDB = self.connect()
            create_table_query = f'''CREATE TABLE IF NOT EXISTS {self.updateTableName()} (
                                email TEXT,
                                user_name TEXT,
                                name_surname TEXT,
                                email_userlk TEXT,
                                user_namelk TEXT,
                                birth_year TEXT,
                                birth_month TEXT,
                                birth_day TEXT,
                                country TEXT);'''

            cursor = connectionDB.cursor()
            print('Successfully Connected to SQLite')
            cursor.execute(create_table_query)
            connectionDB.commit()
            print('SQLite table created')
            cursor.close()
        except sql.Error as error:
            print("Error while creating a sqlite table", error)
        finally:
            #if connectionDB:
            connectionDB.close()
            print("Sqlite connection is closed")

    def insertData(self,recordList):
       
        try:
            connectionDB = self.connect()
            cursor = connectionDB.cursor()
            print('Connected to SQLite')
            insert_user_query = f""" INSERT INTO {self.updateTableName()} 
            (email, user_name, name_surname, 
            birth_day, birth_month, birth_year, 
            country, email_userlk, user_namelk
            ) 
            VALUES (?,?,?,?,?,?,?,?,?); """
            
            cursor.executemany(insert_user_query,recordList)
            connectionDB.commit()
            print("All columns inserted successfully")

        except sql.Error as error:
            print("Failed to insert data into sqlite table", error)

        finally:
            if connectionDB:
                connectionDB.close()
                print('The sqlite connection is closed')