from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship

from .Base import Base

class PaymentInfo(Base):
    __tablename__ = 'PaymentInfo'

    payment_id = Column(Integer, primary_key=True)
    card_number = Column(String)
    cvv = Column(Integer)
    expiration = Column(Date)
    billing = relationship("Address", cascade="all,delete", backref="payment")
    billing_address_id = Column(Integer, ForeignKey("Address.address_id"))
