from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from .Base import Base 

import hashlib

class Customer(Base):
    __tablename__ = "Customer"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    passwordHash = Column(String)

    shipping_address_id = Column(Integer, ForeignKey("Address.address_id"))
    payment_information_id = Column(Integer, ForeignKey("PaymentInfo.payment_id"))

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