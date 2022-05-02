import hashlib

from Models import Address, Customer, PaymentInfo, ShoppingCart
from Helpers import getSession

def checkPassword(customer: Customer, password: str) -> bool:
        return customer.password_hash == hashPassword(password)

def hashPassword(password: str) -> str:
        return hashlib.sha256(password.encode('utf_8')).hexdigest()

def login(username: str, password: str) -> Customer:
    session = getSession()
    userResult = session.query(Customer).filter_by(username=username).first()
    if userResult and checkPassword(userResult, password):
        return userResult
    return None

def register(name: str, username: str, password: str) -> Customer:
    session = getSession()
    userResult = session.query(Customer).filter_by(username=username).first()
    print(userResult)
    if not userResult:
        customerInstance = Customer(name=name, username=username, password_hash=hashPassword(password))
        session.add(customerInstance)
        session.commit()

        customer = session.query(Customer).filter_by(username=username).first()
        session.add(ShoppingCart(user_id=customer.id))
        session.commit()
        
        return session.query(Customer).filter_by(username=username).first()
        

    return None

def attatchPaymentInfoToUser(user: Customer, payment: PaymentInfo) -> None:
    session = getSession()
    session.query(Customer).filter_by(id=user.id).update({"payment_information_id": payment.payment_id})
    session.commit()

def getShippingAddress(user: Customer) -> Address:
    session = getSession()
    return session.query(Address).filter_by(address_id=user.shipping_address_id).first()

def replaceShippingAddress(user: Customer, oldAddress: Address, newAddress: Address):
    session = getSession()
    session.query(Address).filter_by(address_id=oldAddress.address_id).delete()
    session.query(Customer).filter_by(id=user.id).update({"shipping_address_id": newAddress.address_id})
    session.commit()