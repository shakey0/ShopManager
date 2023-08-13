from lib.order import *
from lib.item_in_order import *
from decimal import *

class OrderRepository:

    def __init__(self, connection):
        self._connection = connection

    def get_total_price_for_order(self, id):
        rows = self._connection.execute('SELECT items.price, items_orders.quantity FROM items '
                                        'JOIN items_orders ON items_orders.item_id = items.id '
                                        'JOIN orders ON orders.id = items_orders.order_id '
                                        'WHERE orders.id = %s', [id])
        total_price = 0
        for row in rows:
            total_price += float(Decimal(row['price'])) * row['quantity']
        return round(total_price, 2)

    def get_all(self, list_arrangement, reverse=False):
        rows = self._connection.execute('SELECT * FROM orders')
        all_orders = []
        for row in rows:
            total_price = self.get_total_price_for_order(row['id'])
            all_orders.append(Order(row['id'], row['customer_name'], row['date'], total_price))
        if list_arrangement == "date":
            return sorted(all_orders, key=lambda order: order.date, reverse=reverse)
        elif list_arrangement == "customer_name":
            return sorted(all_orders, key=lambda order: order.customer_name, reverse=reverse)
        elif list_arrangement == "id":
            return sorted(all_orders, key=lambda order: order.id, reverse=reverse)
        elif list_arrangement == "total_price":
            return sorted(all_orders, key=lambda order: order.total_price, reverse=reverse)
        else:
            raise Exception("Unrecognised word for list arrangement was passed!")

    def find_by_id(self, id):
        rows = self._connection.execute('SELECT * FROM orders WHERE orders.id = %s', [id])
        total_price = self.get_total_price_for_order(id)
        row = rows[0]
        return Order(row['id'], row['customer_name'], row['date'], total_price)

    def find_by_customer_name(self, customer_name):
        all_orders = self.get_all("id")
        return [order for order in all_orders if customer_name.lower() in order.customer_name.lower()]

    def find_by_id_and_show_item_details(self, id):
        rows = self._connection.execute('SELECT items.id, items.name, items_orders.quantity, items.price FROM items '
                                        'JOIN items_orders ON items_orders.item_id = items.id '
                                        'JOIN orders ON orders.id = items_orders.order_id '
                                        'WHERE orders.id = %s', [id])
        item_details = [ItemInOrder(row['id'], row['name'], row['quantity'], round(row['quantity'] * float(Decimal(row['price'])), 2)) for row in rows]
        return sorted(item_details, key=lambda item: item.id)
    
    def add_order(self, customer_name, items):
        self._connection.execute('INSERT INTO orders (customer_name, date) VALUES (%s, %s)', [customer_name, '2023/08/08'])
        order_number = len(self.get_all('id'))
        for item in items:
            self._connection.execute('INSERT INTO items_orders (item_id, quantity, order_id) VALUES (%s, %s, %s)',
                                    [item['item_id'], item['quantity'], order_number])

    def remove_items_from_order(self, id, items):
        items_in_order = self.find_by_id_and_show_item_details(id)
        for item_in_order in items_in_order:
            for item in items:
                if item_in_order.id == item['item_id']:
                    if item_in_order.quantity - item['quantity'] < 1:
                        self._connection.execute('DELETE FROM items_orders WHERE item_id = %s AND order_id = %s',
                                                [item_in_order.id, id])
                    else:
                        self._connection.execute('UPDATE items_orders SET quantity = %s WHERE item_id = %s AND order_id = %s',
                                                [item_in_order.quantity - item['quantity'], item_in_order.id, id])
        if self.find_by_id_and_show_item_details(id) == []:
            self.delete_order(id)
            return True

    def delete_order(self, id):
        self._connection.execute('DELETE FROM orders WHERE id = %s', [id])
