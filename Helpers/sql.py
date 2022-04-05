import sqlite3
import os

DB_FILE_NAME = "/database.db"
PARENT_DIRECTORY = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def createDatabase():
    if os.path.exists(PARENT_DIRECTORY+DB_FILE_NAME):
        os.remove(PARENT_DIRECTORY+DB_FILE_NAME)
    connection = sqlite3.connect(PARENT_DIRECTORY+DB_FILE_NAME)
    cursor = connection.cursor()

    sql_file = open(PARENT_DIRECTORY+"/Helpers/sql/init.sql").read()
    cursor.executescript(sql_file)

    for row in cursor.execute("SELECT * FROM Book"):
        print(row)
    for row in cursor.execute("SELECT * FROM InventoryItem"):
        print(row)
    for row in cursor.execute("SELECT * FROM Book b, InventoryItem i WHERE i.book_reference = b.id"):
        print(row)

def getDatabase():
    return sqlite3.connect(PARENT_DIRECTORY+DB_FILE_NAME)

if __name__ == "__main__":
    createDatabase()