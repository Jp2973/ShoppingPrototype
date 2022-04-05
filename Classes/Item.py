class Item:
    def __init__(self):
        self.quantity: str = None
        self.title: str = None
        self.description: str = None
        self.genre: str = None
        self.price: float = None
    
    def __str__(self):
        return self.title
    
    def __repr__(self):
        return self.title