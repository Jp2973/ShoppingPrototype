import sqlite3, os, sys

from Classes import Customer, Book
from Controllers.BooksController import getAllBooks

def welcomeView():
    while 1:
        print("Please Select From The Following Options:\n[l] - Login\n[r] - Register\n[x] - Exit\n")
        option = input("Your Input: ").lower()
        if option == "l":
            loginView()
        elif option == "r":
            registerView()
        elif option == "x":
            return

def loginView():
    print("Login:")
    email = input("\tEmail: ")
    password = input("\tPassword: ")
    debugCustomer = Customer("test@test.com", "password", "test")
    if debugCustomer.authenticateCustomer(password):
        mainView()
    else:
        print("Unsuccessful Login Returning to Main Menu\n")
    return


def registerView():
    print("Register:")
    name = input("\tName (optional): ")
    email = input("\tEmail: ")
    password = input("\tPassword: ")
    customerObject = Customer(email, password, name if len(name) else None)

def mainView():
    while 1:
        print("Please Select From The Following Options:\n[b] - view all books\n[m] - view all movies\n[l] - Logout\n[x] - Exit\n")
        option = input("Your Input: ").lower()
        if option == "b":
            bookView()
        elif option == "m":
            pass
        elif option == "l":
            return
        elif option == "x":
            sys.exit(0)

def bookView():
    books = getAllBooks()
    for index, book in enumerate(books):
        print (f'{index}: {book.title} {book.author} {book.quantity}')
    print()

def basicTest():
    welcomeView()

if __name__ == "__main__":
    basicTest()