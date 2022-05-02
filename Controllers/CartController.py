from Models import Customer, CartItem, ShoppingCart
from Helpers import getSession
from Models.Item import InventoryItem

def getUserCart(user: Customer) -> ShoppingCart:
    session = getSession()
    return session.query(ShoppingCart).filter_by(user_id=user.id).first()

def getItemsInCart(cart: ShoppingCart):
    session = getSession()
    return session.query(CartItem).filter_by(cart_id=cart.cart_id).all()

def updateCartItem(cart: ShoppingCart, item: InventoryItem, quantity: int):
    session = getSession()
    cartQuery = session.query(ShoppingCart).filter_by(cart_id=cart.cart_id)
    cartItem = session.query(CartItem).filter_by(cart_id=cart.cart_id).filter_by(item_id=item.InventoryItem.item_id)

    priceDiff = 0
    if cartItem.first():
        priceDiff = (quantity - cartItem.first().quantity) * item.InventoryItem.price 
        if quantity == 0:
            cartItem.delete()
        else:
            cartItem.update({CartItem.quantity: quantity, CartItem.subtotal: cartItem.first().subtotal - priceDiff})
    else:
        if quantity != 0:
            priceDiff = (quantity * item.InventoryItem.price)
            cItem = CartItem(quantity=quantity, cart_id=cart.cart_id, subtotal=priceDiff, item_id=item.InventoryItem.item_id)
            session.add(cItem)
    cartQuery.update({"total": cartQuery.first().total + priceDiff})
    session.commit()

def resetUserCart(user: Customer) -> bool:
    session = getSession()
    oldCart = session.query(ShoppingCart).filter_by(user_id=user.id).first()
    if oldCart:
        session.delete(oldCart)
    session.add(ShoppingCart(user_id=user.id, total=0))
    session.commit()
    return True
