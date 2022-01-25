import sqlite3 as sql
from datetime import datetime
from operations.file_operations import FileOperations

class DBOperations():
    
    def __init__(self, db_name):
        self.db_name = db_name

    def connect(self):
        """
        Create a database connection to SQLite database
        :returns: sqlite3.connection 
        """
        connection = sql.connect(self.db_name)
        return connection

    def updateTableName(self):
        """
        Updates the data name with the date format
        """
        return 'data_{}'.format(datetime.now().strftime("%d%m%Y"))

    def createTable(self):
        """
        Connects to the database and creates a new table
        """
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
        """
        Adds all data to database
        :param recordList: <list>
        """
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

    def showTable(self):
        """
        Shows the exists database tables
        """
        connectionDB = self.connect()
        cursor = connectionDB.cursor()
        cursor.execute(f"SELECT name FROM {self.updateTableName()}")
        data = cursor.fetchall()
        for row in data:
            print(row)