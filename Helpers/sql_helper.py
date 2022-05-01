import os, sys
from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker

DB_FILE_NAME = "/database.db"
PARENT_DIRECTORY = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.append(PARENT_DIRECTORY)
from Models import *


engine = create_engine('sqlite://' + DB_FILE_NAME, echo=True)

_SESSION = sessionmaker(bind=engine)

def createDatabase():
    getSession()
    insp = inspect(engine)
    print(insp.get_table_names())   

def getSession():
    Base.metadata.create_all(bind=engine)
    return _SESSION()

if __name__ == "__main__":
    createDatabase()