from .Item import Item

class Book(Item):
    def __init__(self):
        Item.__init__(self)
        self.isbn: str = None
        self.author: str = None
        self.publisher: str = None
        