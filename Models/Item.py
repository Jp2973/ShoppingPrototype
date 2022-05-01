from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

from .Base import Base

class InventoryItem(Base):
    __tablename__ = "InventoryItem"
    item_id = Column(Integer, primary_key=True)
    quantity = Column(Integer)
    title = Column(String)
    description = Column(String)
    price = Column(Float)
    item_type = Column(String)

    book_reference = Column(Integer, ForeignKey("Book.id"))
    movie_reference = Column(Integer, ForeignKey("Movie.id"))
    
    def __str__(self):
        return self.title
    
    def __repr__(self):
        return self.title