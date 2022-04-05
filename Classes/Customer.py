import hashlib
from typing import List

from sympy import true

from .Order import Order
from .ShoppingCart import ShoppingCart
from .Address import Address
from .PaymentInfo import PaymentInfo



class Customer:
    def __init__(self, email: str, password: str, name: str = None):
        self.__id: int = None
        self.name: str = name
        self.shippingAddress: Address = None
        self.paymentInfo: PaymentInfo = None
        self.__email: str = email
        self.__passwordHash: str = self.__hashPassword(password)
        self.shoppingCarts: List[ShoppingCart] = []
        self.orders: List[Order] = []

    def getID(self) -> int:
        return self.__id
    
    def getEmail(self) -> str:
        return self.__email
    
    def authenticateCustomer(self, password) -> bool:
        return self.__checkPassword(password)
    
    def changePassword(self, previousPassword, newPassword) -> bool:
        if self.__checkPassword(previousPassword):
            self.__passwordHash = self.__hashPassword(newPassword)
            return True
        else:
            return False
    
    def addShoppingCart(self, shoppingCart: ShoppingCart):
        self.shoppingCarts.append(shoppingCart)
    
    def removeShoppingCart(self, shoppingCart: ShoppingCart):
        if shoppingCart in self.shoppingCarts:
            self.shoppingCarts.remove(shoppingCart)
    
    def addOrder(self, order: Order):
        self.order.append(order)
    
    def deleteAccount(self, password) -> bool:
        if self.__checkPassword(password):
            del self.shoppingCarts[:]
            del self.orders
            return True
        return False
        

    def __checkPassword(self, password: str) -> bool:
        return self.__passwordHash == self.__hashPassword(password)

    def __hashPassword(self, password: str) -> str:
        return hashlib.sha256(password.encode('utf_8')).hexdigest()