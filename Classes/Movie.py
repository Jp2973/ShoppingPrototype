from .Item import Item

class Movie(Item):
    def __init__(self):
        Item.__init__(self)
        self.director: str = None
        self.leadingActor: str = None
        