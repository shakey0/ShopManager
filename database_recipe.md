Two Tables (Many-to-Many) Design Recipe Template
Copy this recipe template to design and create two related database tables having a Many-to-Many relationship.

1. Extract nouns from the user stories or specification

As a shop manager
So I can know which items I have in stock
I want to keep a list of my shop items with their name and unit price.

As a shop manager
So I can know which items I have in stock
I want to know which quantity (a number) I have for each item.

As a shop manager
So I can manage items
I want to be able to create a new item.

As a shop manager
So I can know which orders were made
I want to keep a list of orders with their customer name.

As a shop manager
So I can know which orders were made
I want to assign each order to their corresponding item.

As a shop manager
So I can know which orders were made
I want to know on which date an order was placed. 

As a shop manager
So I can manage orders
I want to be able to create a new order.

Nouns: 
items, name, price, stock, amount_sold
orders, customer_name, date


2. Infer the Table Name and Columns
Put the different nouns in this table. Replace the example with your own nouns.

Record	Properties
items	name, price, stock, amount_sold
orders	customer_name, date

Name of the first table (always plural): items

Column names: name, price, stock, amount_sold

Name of the second table (always plural): orders

Column names: customer_name, date


3. Decide the column types.
Here's a full documentation of PostgreSQL data types.

Most of the time, you'll need either text, int, bigint, numeric, or boolean. If you're in doubt, do some research or ask your peers.

Remember to always have the primary key id as a first column. Its type will always be SERIAL.

Table: items
id: SERIAL
name: text
price: DECIMAL
stock: int
amount_sold int

Table: orders
id: SERIAL
customer_name: text
date: date


4. Design the Many-to-Many relationship
Make sure you can answer YES to these two questions:

Can one item have many orders? YES
Can one order have many items? YES

If you would answer "No" to one of these questions, you'll probably have to implement a One-to-Many relationship, which is simpler. Use the relevant design recipe in that case.


5. Design the Join Table
The join table usually contains two columns, which are two foreign keys, each one linking to a record in the two other tables.

The join table is: items_orders

Columns: item_id, quantity, order_id


6. Write the SQL.
-- EXAMPLE
-- file: items_orders.sql

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


5. Create the tables.
psql -h 127.0.0.1 items_orders < seeds/items_orders.sql
