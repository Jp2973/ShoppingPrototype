from datetime import datetime
from typing import List

from .Item import Item
from .Address import Address
from .PaymentInfo import PaymentInfo

class Order:
    def __init__(self):
        self.__orderDate: datetime = None
        self.deliveryAddress: Address = None
        self.paymentInfo: PaymentInfo = None
        self.items: List[Item] = []

    @property
    def orderDate(self):
        return self.orderDate

    @orderDate.setter
    def orderDate(self, date: str):
        self.orderDate = datetime.strptime(date, '%b %d %Y %I:%M%p')