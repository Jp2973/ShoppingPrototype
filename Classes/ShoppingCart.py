from typing import List

from sympy import true

from .Item import Item

class ShoppingCart:
    def __init__(self):
        self.items: List[Item] = []
        self.subtotal: float = 0.0
        self.total: float = 0

    def setItem(self, item: Item, quantity: int) -> bool:
        #TO-DO Validate Quantity In Stock, Modify Stock, Modify Subtotal
        self.items[item] = quantity
        return True
    
    def removeItem(self, item: Item) -> bool:
        #TO-DO Readd to stock, modify subtotal
        if item in self.items:
            del self.items[item]
            return True
        else:
            return False
    
    def checkout(self):
        #TO-DO Create Order Instance
        print("User Checkout - Debugging Message")