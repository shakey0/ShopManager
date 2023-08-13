from lib.item_repository import *
from lib.order_repository import *

def place_order(connection, customer_name, items):
    item_repository = ItemRepository(connection)
    order_repository = OrderRepository(connection)
    unadded_items = []
    for item in items:
        valid = item_repository.update_item(item['item_id'], adjust_stock=item['quantity']*-1,
                                            add_amount_sold=item['quantity'])
        if valid == False:
            unadded_items.append(item)
    if len(items) != len(unadded_items):
        order_repository.add_order(customer_name, [item for item in items if item not in unadded_items])
    if unadded_items == []:
        return "All items ordered successfully."
    elif len(unadded_items) != len(items):
        return "Insufficient stock for some of the items you ordered.\nAvailable items were ordered. Check your order details.\nYou may try ordering a fewer amount of the unsuccessful items."
    else:
        return "Insufficient stock. Your order was not placed."
    
def get_partial_refund(connection, order_id, items):
    item_repository = ItemRepository(connection)
    order_repository = OrderRepository(connection)
    for item in items:
        item_repository.update_item(item['item_id'], adjust_stock=item['quantity'],
                                    add_amount_sold=item['quantity']*-1)
    was_cancelled = order_repository.remove_items_from_order(order_id, items)
    if was_cancelled:
        return "Your order has been cancelled and refunded."
    return "Your selected items have been refunded."

def get_full_refund(connection, order_id):
    item_repository = ItemRepository(connection)
    order_repository = OrderRepository(connection)
    items_in_order = order_repository.find_by_id_and_show_item_details(order_id)
    for item_in_order in items_in_order:
        item_repository.update_item(item_in_order.id, adjust_stock=item_in_order.quantity,
                                    add_amount_sold=item_in_order.quantity*-1)
    order_repository.delete_order(order_id)
    return "Your order has been cancelled and refunded."