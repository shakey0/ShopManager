from lib.item import *
from lib.order_in_item import *
import datetime
from decimal import *

class ItemRepository:

    def __init__(self, connection):
        self._connection = connection

    def get_last_date_sold(self, id):
        rows = self._connection.execute('SELECT * FROM orders '
                                        'JOIN items_orders ON items_orders.order_id = orders.id '
                                        'JOIN items ON items.id = items_orders.item_id '
                                        'WHERE items.id = %s', [id])
        if len(rows) > 0:
            return sorted(rows, key=lambda row: row['date'])[-1]['date']
        return datetime.date(1, 1, 1)

    def get_all(self, list_arrangement, reverse=False):
        rows = self._connection.execute('SELECT * FROM items')
        all_items = []
        for row in rows:
            last_date_sold = self.get_last_date_sold(row['id'])
            all_items.append(Item(row['id'], row['name'], float(Decimal(row['price'])),
                                  row['stock'], row['amount_sold'], last_date_sold))
        if list_arrangement == "price":
            return sorted(all_items, key=lambda item: item.price, reverse=reverse)
        elif list_arrangement == "stock":
            return sorted(all_items, key=lambda item: item.stock, reverse=reverse)
        elif list_arrangement == "amount_sold":
            return sorted(all_items, key=lambda item: item.amount_sold, reverse=reverse)
        elif list_arrangement == "name":
            return sorted(all_items, key=lambda item: item.name, reverse=reverse)
        elif list_arrangement == "id":
            print(all_items)
            return sorted(all_items, key=lambda item: item.id, reverse=reverse)
        elif list_arrangement == "last_date_sold":
            return sorted(all_items, key=lambda item: item.last_date_sold, reverse=reverse)
        else:
            raise Exception("Unrecognised word for list arrangement was passed!")

    def find_by_id(self, id):
        rows = self._connection.execute('SELECT * FROM items WHERE items.id = %s', [id])
        last_date_sold = self.get_last_date_sold(id)
        row = rows[0]
        return Item(row['id'], row['name'], float(Decimal(row['price'])),
                    row['stock'], row['amount_sold'], last_date_sold)

    def find_by_name(self, name):
        all_items = self.get_all("id")
        return [item for item in all_items if name.lower() in item.name.lower()]

    def find_by_id_and_show_order_details(self, id):
        rows = self._connection.execute('SELECT orders.id, orders.customer_name, items_orders.quantity, orders.date FROM orders '
                                        'JOIN items_orders ON items_orders.order_id = orders.id '
                                        'JOIN items ON items.id = items_orders.item_id '
                                        'WHERE items.id = %s', [id])
        return [OrderInItem(row['id'], row['customer_name'], row['quantity'], row['date']) for row in rows]
    
    def add_item(self, name, price, stock):
        self._connection.execute('INSERT INTO items (name, price, stock, amount_sold) VALUES (%s, %s, %s, %s)',
                                [name, price, stock, 0])

    def update_item(self, id, price=0, adjust_stock=0, add_amount_sold=0):
        if price > 0:
            self._connection.execute('UPDATE items SET price = %s WHERE id = %s', [price, id])
        if adjust_stock != 0:
            item_stock = self.find_by_id(id).stock
            if item_stock + adjust_stock < 0:
                return False
            else:
                self._connection.execute('UPDATE items SET stock = %s WHERE id = %s', [item_stock + adjust_stock, id])
        if add_amount_sold != 0:
            amount_sold = self.find_by_id(id).amount_sold
            self._connection.execute('UPDATE items SET amount_sold = %s WHERE id = %s', [amount_sold + add_amount_sold, id])

    def delete_item(self, id):
        if self.find_by_id_and_show_order_details(id) != []:
            return False
        self._connection.execute('DELETE FROM items WHERE id = %s', [id])