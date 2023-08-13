DROP TABLE IF EXISTS items CASCADE;
DROP SEQUENCE IF EXISTS items_id_seq;

DROP TABLE IF EXISTS orders CASCADE;
DROP SEQUENCE IF EXISTS orders_id_seq;

DROP TABLE IF EXISTS items_orders;
DROP SEQUENCE IF EXISTS items_orders_id_seq;

-- Create the first table.
CREATE TABLE items (
  id SERIAL PRIMARY KEY,
  name text,
  price DECIMAL,
  stock int,
  amount_sold int
);

-- Create the second table.
CREATE TABLE orders (
  id SERIAL PRIMARY KEY,
  customer_name text,
  date date
);

-- Create the join table.
CREATE TABLE items_orders (
  item_id int,
  quantity int,
  order_id int,
  constraint fk_item foreign key(item_id) references items(id) on delete cascade,
  constraint fk_order foreign key(order_id) references orders(id) on delete cascade,
  PRIMARY KEY (item_id, order_id)
);

INSERT INTO items (name, price, stock, amount_sold) VALUES ('Blueberry Soap', 3.49, 34, 14);
INSERT INTO items (name, price, stock, amount_sold) VALUES ('Carrot Soap', 3.49, 40, 8);
INSERT INTO items (name, price, stock, amount_sold) VALUES ('Raspberry Soap', 3.49, 31, 17);
INSERT INTO items (name, price, stock, amount_sold) VALUES ('Apple Soap', 3.49, 28, 20);
INSERT INTO items (name, price, stock, amount_sold) VALUES ('Orange Soap', 3.49, 27, 21);
INSERT INTO items (name, price, stock, amount_sold) VALUES ('Banana Soap', 3.49, 42, 6);
INSERT INTO items (name, price, stock, amount_sold) VALUES ('Tea Soap', 3.49, 64, 32);
INSERT INTO items (name, price, stock, amount_sold) VALUES ('Coffee Soap', 3.49, 33, 15);
INSERT INTO items (name, price, stock, amount_sold) VALUES ('Peach Soap', 3.49, 18, 78);
INSERT INTO items (name, price, stock, amount_sold) VALUES ('Rose Soap', 3.49, 50, 46);

INSERT INTO orders (customer_name, date) VALUES ('Merry', '2023/08/06');
INSERT INTO orders (customer_name, date) VALUES ('Andrew', '2023/08/07');
INSERT INTO orders (customer_name, date) VALUES ('Alex', '2023/08/07');
INSERT INTO orders (customer_name, date) VALUES ('Ben', '2023/08/07');
INSERT INTO orders (customer_name, date) VALUES ('Amy', '2023/08/07');
INSERT INTO orders (customer_name, date) VALUES ('Kate', '2023/08/07');
INSERT INTO orders (customer_name, date) VALUES ('Rose', '2023/08/07');
INSERT INTO orders (customer_name, date) VALUES ('Art', '2023/08/07');
INSERT INTO orders (customer_name, date) VALUES ('John', '2023/08/07');
INSERT INTO orders (customer_name, date) VALUES ('Ricky', '2023/08/07');
INSERT INTO orders (customer_name, date) VALUES ('Cathy', '2023/08/07');
INSERT INTO orders (customer_name, date) VALUES ('Ann', '2023/08/07');
INSERT INTO orders (customer_name, date) VALUES ('Scott', '2023/08/07');
INSERT INTO orders (customer_name, date) VALUES ('Benson', '2023/08/07');
INSERT INTO orders (customer_name, date) VALUES ('Kevin', '2023/08/07');
INSERT INTO orders (customer_name, date) VALUES ('Stacey', '2023/08/07');
INSERT INTO orders (customer_name, date) VALUES ('Tracey', '2023/08/07');
INSERT INTO orders (customer_name, date) VALUES ('Emma', '2023/08/07');
INSERT INTO orders (customer_name, date) VALUES ('Laura', '2023/08/07');
INSERT INTO orders (customer_name, date) VALUES ('Kay', '2023/08/07');
INSERT INTO orders (customer_name, date) VALUES ('Owen', '2023/08/08');

INSERT INTO items_orders (item_id, quantity, order_id) VALUES (1, 1, 1);
INSERT INTO items_orders (item_id, quantity, order_id) VALUES (1, 1, 4);
INSERT INTO items_orders (item_id, quantity, order_id) VALUES (1, 1, 5);
INSERT INTO items_orders (item_id, quantity, order_id) VALUES (1, 2, 9);
INSERT INTO items_orders (item_id, quantity, order_id) VALUES (1, 1, 19);
INSERT INTO items_orders (item_id, quantity, order_id) VALUES (1, 1, 20);
INSERT INTO items_orders (item_id, quantity, order_id) VALUES (2, 1, 6);
INSERT INTO items_orders (item_id, quantity, order_id) VALUES (2, 2, 11);
INSERT INTO items_orders (item_id, quantity, order_id) VALUES (2, 2, 14);
INSERT INTO items_orders (item_id, quantity, order_id) VALUES (3, 1, 9);
INSERT INTO items_orders (item_id, quantity, order_id) VALUES (3, 1, 14);
INSERT INTO items_orders (item_id, quantity, order_id) VALUES (3, 5, 16);
INSERT INTO items_orders (item_id, quantity, order_id) VALUES (3, 1, 21);
INSERT INTO items_orders (item_id, quantity, order_id) VALUES (4, 1, 2);
INSERT INTO items_orders (item_id, quantity, order_id) VALUES (4, 1, 3);
INSERT INTO items_orders (item_id, quantity, order_id) VALUES (4, 1, 17);
INSERT INTO items_orders (item_id, quantity, order_id) VALUES (5, 1, 10);
INSERT INTO items_orders (item_id, quantity, order_id) VALUES (5, 1, 12);
INSERT INTO items_orders (item_id, quantity, order_id) VALUES (5, 3, 13);
INSERT INTO items_orders (item_id, quantity, order_id) VALUES (5, 2, 14);
INSERT INTO items_orders (item_id, quantity, order_id) VALUES (6, 3, 6);
INSERT INTO items_orders (item_id, quantity, order_id) VALUES (6, 1, 12);
INSERT INTO items_orders (item_id, quantity, order_id) VALUES (6, 1, 17);
INSERT INTO items_orders (item_id, quantity, order_id) VALUES (6, 1, 20);
INSERT INTO items_orders (item_id, quantity, order_id) VALUES (7, 1, 4);
INSERT INTO items_orders (item_id, quantity, order_id) VALUES (7, 1, 7);
INSERT INTO items_orders (item_id, quantity, order_id) VALUES (7, 6, 11);
INSERT INTO items_orders (item_id, quantity, order_id) VALUES (7, 2, 12);
INSERT INTO items_orders (item_id, quantity, order_id) VALUES (7, 1, 14);
INSERT INTO items_orders (item_id, quantity, order_id) VALUES (8, 1, 8);
INSERT INTO items_orders (item_id, quantity, order_id) VALUES (8, 1, 9);
INSERT INTO items_orders (item_id, quantity, order_id) VALUES (8, 2, 19);
INSERT INTO items_orders (item_id, quantity, order_id) VALUES (9, 1, 15);
INSERT INTO items_orders (item_id, quantity, order_id) VALUES (9, 2, 16);
INSERT INTO items_orders (item_id, quantity, order_id) VALUES (9, 1, 18);
INSERT INTO items_orders (item_id, quantity, order_id) VALUES (10, 2, 10);
INSERT INTO items_orders (item_id, quantity, order_id) VALUES (10, 1, 13);
INSERT INTO items_orders (item_id, quantity, order_id) VALUES (10, 4, 15);
INSERT INTO items_orders (item_id, quantity, order_id) VALUES (10, 2, 21);