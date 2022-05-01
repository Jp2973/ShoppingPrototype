CREATE TABLE Movie (
    id integer PRIMARY KEY,
    director text,
    leading_actor text
);

CREATE TABLE Book (
    id integer PRIMARY KEY,
    author text,
    publisher text,
    isbn text
);

CREATE TABLE InventoryItem (
    item_id integer PRIMARY KEY,
    quantity integer,
    title text,
    description text,
    genre text,
    price real,
    item_type text,
    book_reference integer,
    movie_reference integer,
    FOREIGN KEY(book_reference) REFERENCES Book(id),
    FOREIGN KEY(movie_reference) REFERENCES Movie(id)
);

CREATE TABLE Address (
    address_id integer PRIMARY KEY,
    street_one text,
    street_two text,
    city text,
    state text,
    zip integer
);

CREATE TABLE PaymentInfo (
    payment_id integer PRIMARY KEY,
    card_number text,
    cvv integer,
    expiration text,
    billing_address_id integer,
    FOREIGN KEY(billing_address_id) REFERENCES Address(address_id)
);

CREATE TABLE Customer (
    id integer PRIMARY KEY,
    name text,
    email text,
    password_hash text,
    shipping_address_id integer,
    payment_information_id integer,
    FOREIGN KEY(shipping_address_id) REFERENCES Address(address_id),
    FOREIGN KEY(payment_information_id) REFERENCES PaymentInfo(payment_id)
);

CREATE TABLE ShoppingCart (
    cart_id integer PRIMARY KEY,
    subtotal real,
    total real,
    user_id integer,
    FOREIGN KEY(user_id) REFERENCES Customer(id)
);

CREATE TABLE CartItem (
    id integer PRIMARY KEY,
    subtotal real,
    quantity integer,
    cart_id integer,
    item_id integer,
    FOREIGN KEY(cart_id) REFERENCES ShoppingCart(cart_id),
    FOREIGN KEY(item_id) REFERENCES InventoryItem(item_id)
);

CREATE TABLE Order (
    order_id integer PRIMARY KEY,
    subtotal real,
    total real,
    user_id integer,
    address_id integer,
    payment_id integer,
    FOREIGN KEY(user_id) REFERENCES Customer(id)
    FOREIGN KEY(address_id) REFERENCES Address(address_id),
    FOREIGN KEY(payment_id) REFERENCES PaymentInfo(payment_id)
);

CREATE TABLE OrderItem (
    id integer PRIMARY KEY,
    subtotal real,
    quantity integer,
    order_id integer,
    item_id integer,
    FOREIGN KEY(order_id) REFERENCES Order(order_id),
    FOREIGN KEY(item_id) REFERENCES InventoryItem(item_id)
);

INSERT INTO Book (author, publisher, isbn) VALUES ("John Doe", "Wholehouse", "10928901");
INSERT INTO InventoryItem (quantity, title, description, genre, price, item_type, book_reference) VALUES (7, "Generic Title", "Generic Description", "Generic Genre", 20.70, "B", 1)
