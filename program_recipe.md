1. Describe the Problem

- Create a new item
- Update an existing item
- Delete an item
- Find a specific item by its number - option to show (order_)id(s), customer_name(s), date(s)
- Find a specific item by letters in its name - (order_)id(s), customer_name(s), date(s)
- List all items by price, stock, amount_sold, alphabetically, (item_)id, last_date_sold

- Create a new order (update item stock and amount sold)
- Update an existing order (update item stock and amount sold for items removed)
- Delete an order (update item stock and amount sold for items in order)
- Find a specific order by its number
- Find a specific order by letter in the customer_name
- List all orders by total_price, alphabetically(customer_name), date, (order_)id


2. Design the Class System

TakeawayOrderer: (Main Class)

```python

class Item:

    def __init__(self, id, name, price, stock, amount_sold):
        # stores the item data passed in
        pass

    def __eq__(self, other):
        return self.__dict__ == other.__dict__


class ItemRepository:

    def __init__(self, connection):
        self._connection = connection

    def get_all(self, list_arrangement):
        # returns a list of all the items ordered by the user's preference
        # (price, stock, amount_sold, alphabetically, (item_)id, last_date_sold)

    def find_by_id(self, id):
        # returns the item according to the id number given

    def find_by_name(self, name):
        # returns a list of items with matching characters in their names

    def find_by_id_and_show_order_details(self, id):
        # returns a list of order_ids, customer_names, and dates for the item
    
    def add(self, name, price, stock):
        # adds the Item to the database

    def update(self, id, price=0, stock=0, amount_sold=0):
        # updates the price with the new price if passed in
        # subtracts from the stock depending on what is passed in (or refuses if self.stock is 0)
        # adds the number passed in to the amount_sold
        # returns True if sucessful or False if unsuccessful

    def delete(self, id):
        # deletes the item only if it isn't linked with any order data


class Order:

    def __init__(self, id, customer_name, date):
        # stores the order data passed in
        pass

    def __eq__(self, other):
        return self.__dict__ == other.__dict__


class OrderRepository:

    def __init__(self, connection):
        self._connection = connection

    def get_all(self, list_arrangement):
        # returns a list of all the orders placed by the user's preference
        # (date, alphabetically, (item_)id, total_price)

    def find_by_id(self, id):
        # returns the order according to the id number given

    def find_by_name(self, name):
        # returns a list of orders with matching characters in their customer names

    def find_by_id_and_show_item_details(self, id):
        # returns a list of item information (item_id, name, price, quantity) for the order
    
    def add(self, customer_name, items):
        # adds the Order to the database AND amends the stock and amount_sold in the Item table

    def remove_items_from_order(self, id, items):
        # subtracts the number of each item passed in from the quanitity
        # if the quantitiy hits 0, the link in the orders_items table will be removed
        # adds to the stock in the Item depending on what is passed in
        # subtracts from the amount_sold in the Item
        # returns True if sucessful or False if unsuccessful
        # calls the delete method if all the Items in the order are being removed

    def delete(self, id):
        # deletes the order and amends the stock and amount_sold in the Item accordingly


# Class in app.py
class ShopManager:

    def __init__(self):
        pass
