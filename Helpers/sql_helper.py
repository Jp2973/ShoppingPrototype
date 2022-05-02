import os, sys
from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker
import pandas as pd

DB_FILE_NAME = "/database.db"
CURRENT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))
PARENT_DIRECTORY = os.path.dirname(CURRENT_DIRECTORY)

sys.path.append(PARENT_DIRECTORY)
from Models import *


engine = create_engine('sqlite://' + DB_FILE_NAME)

_SESSION = sessionmaker(bind=engine)

def createBook(bookInfo):
    session = getSession()
    bookInstance = Book(author=bookInfo["author"], publisher=bookInfo["publisher"], isbn=bookInfo["isbn"])    
    session.add(bookInstance)
    session.commit()

    book = session.query(Book).filter_by(isbn=bookInfo["isbn"]).first()
    itemInstance = InventoryItem(quantity=bookInfo["quantity"], title=bookInfo["title"], description=bookInfo["description"], genre=bookInfo["genre"], price=bookInfo["price"], item_type="B", book_reference=book.id)
    session.add(itemInstance)
    session.commit()

def createMovie(movieInfo):
    session = getSession()
    movieInstance = Movie(director=movieInfo["director"], leading_actor=movieInfo["leading_actor"])    
    session.add(movieInstance)
    session.commit()

    session.refresh(movieInstance)

    itemInstance = InventoryItem(quantity=movieInfo["quantity"], title=movieInfo["title"], description=movieInfo["description"], genre=movieInfo["genre"], price=movieInfo["price"], item_type="M", movie_reference=movieInstance.id)
    session.add(itemInstance)
    session.commit()

def createDatabase():
    dropTables()
    session = getSession()
    insp = inspect(engine)
    print(insp.get_table_names())

    books_df = pd.read_csv(CURRENT_DIRECTORY + "/Initial/Books.csv")
    books_df_dict = books_df.to_dict(orient='records')
    [createBook(book) for book in books_df_dict]

    movies_df = pd.read_csv(CURRENT_DIRECTORY + "/Initial/Movies.csv")
    movies_df_dict = movies_df.to_dict(orient='records')
    [createMovie(movie) for movie in movies_df_dict]

    print(session.query(Book).all())

def getSession():
    Base.metadata.create_all(bind=engine)
    return _SESSION()

def _objectToDict(object):
    return {col.key: getattr(object, col.key) for col in inspect(object).mapper.column_attrs}

def flattenEntries(entryTouples):
    return [{**_objectToDict(a), **_objectToDict(b)} for a, b in entryTouples]

def dropTables():
    Base.metadata.drop_all(bind=engine)

def printTables():
    books = pd.read_sql_table(table_name="Book", con=engine)
    movies = pd.read_sql_table(table_name="Movie", con=engine)
    items = pd.read_sql_table(table_name="InventoryItem", con=engine)
    carts = pd.read_sql_table(table_name="ShoppingCart", con=engine)
    cartItems = pd.read_sql_table(table_name="CartItem", con=engine)
    orders = pd.read_sql_table(table_name="Order", con=engine)
    orderItems = pd.read_sql_table(table_name="OrderItem", con=engine)
    customers = pd.read_sql_table(table_name="Customer", con=engine)
    paymentInfos = pd.read_sql_table(table_name="PaymentInfo", con=engine)
    addresses = pd.read_sql_table(table_name="Address", con=engine)   
    
    print("Books: \n", books)
    print("Items: \n", items)
    print("Carts: \n", carts)
    print("CartItems: \n", cartItems)
    print("Orders: \n", orders)
    print("OrderItems: \n", orderItems)
    print("Customers: \n", customers)
    print("PaymentInfo: \n", paymentInfos)
    print("Addresses: \n", addresses)

if __name__ == "__main__":
    createDatabase()
    printTables()