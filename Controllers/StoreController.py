from Helpers import getSession
from Models import Book, InventoryItem, Movie

def getAllBooks():
    session = getSession()
    return session.query(InventoryItem, Book).join(Book, InventoryItem.book_reference == Book.id).all()

def getAllMovies():
    session = getSession()
    return session.query(InventoryItem, Movie).join(Movie, InventoryItem.book_reference == Movie.id).all()

