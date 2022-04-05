from .Address import Address

class PaymentInfo:
    def __init__(self):
        self.cardNumber: str = None
        self.nameOnCard: str = None
        self.expirationDateMonth: int = None
        self.expirationDateYear: int = None
        self.cvv: int = None
        self.billingAddress: Address = None

    def getExpirationDate(self):
        return {"month": self.expirationDateMonth, "year": self.expirationDateYear}