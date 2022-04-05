from Helpers.sql import getDatabase
from Classes.Book import Book

def getAllBooks():
    dbConnection = getDatabase()
    curser = dbConnection.cursor()
    books = []
    for _id, author, publisher, isbn, _id, quantity, title, description, genre, price, _class, _bid, _mid in curser.execute("SELECT * FROM Book b, InventoryItem i WHERE i.book_reference = b.id"):
        bookInstance = Book()
        bookInstance.author = author
        bookInstance.publisher = publisher
        bookInstance.isbn = isbn
        bookInstance.quantity = quantity
        bookInstance.title = title
        bookInstance.description = description
        bookInstance.genre = genre
        bookInstance.price = price
        books.append(bookInstance)
    return books