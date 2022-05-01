import sys

from Controllers import getItemsInCart, getUserCart
import Helpers.state as state

def cartView():
    while 1:
        cart = getUserCart(state.user_state)
        cartItems = getItemsInCart(cart)
        print(cartItems)
        [print(f"{i}") for i in cartItems]
        print(f"\n[r] - return\n[x] - exit\n")
        option = input("Your Input: ").lower()
        if option == "r":
            return
        elif option == "x":
            sys.exit(0)
