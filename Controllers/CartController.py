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
    cartItem = session.query(CartItem).filter_by(cart_id=cart.cart_id).filter_by(item_id=item.InventoryItem.item_id)

    if cartItem.first():
        if quantity == 0:
            cartItem.delete()
        else:
            cartItem.update({CartItem.quantity: quantity})
    else:
        if quantity != 0:
            cItem = CartItem(quantity=quantity, cart_id=cart.cart_id, item_id=item.InventoryItem.item_id)
            session.add(cItem)
    session.commit()

def resetUserCart(user: Customer) -> bool:
    session = getSession()
    oldCart = session.query(ShoppingCart).filter_by(user_id=user.id).first()
    if oldCart:
        session.delete(oldCart)
    session.add(ShoppingCart(user_id=user.id, subtotal=0, total=0))
    session.commit()
    return True
