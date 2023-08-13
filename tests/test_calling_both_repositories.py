from lib.calling_both_repositories import *
from lib.item_repository import *
from lib.order_repository import *
from lib.order_in_item import *
from lib.item_in_order import *
from lib.item import *
from lib.order import *

def test_place_order(db_connection):
    db_connection.seed('seeds/items_orders.sql')
    order_repository = OrderRepository(db_connection)
    item_repository = ItemRepository(db_connection)
    assert place_order(db_connection, "William", [{"item_id": 3, "quantity": 3}, {"item_id": 5, "quantity": 1},
                                                {"item_id": 9, "quantity": 2}]) == "All items ordered successfully."
    assert order_repository.find_by_id(22) == Order(22, 'William', datetime.date(2023, 8, 8), 20.94)
    assert order_repository.find_by_id_and_show_item_details(22) == [
        ItemInOrder(3, "Raspberry Soap", 3, 10.47),
        ItemInOrder(5, "Orange Soap", 1, 3.49),
        ItemInOrder(9, "Peach Soap", 2, 6.98)
    ]
    assert item_repository.get_all("id") == [
        Item(1, 'Blueberry Soap', 3.49, 34, 14, datetime.date(2023, 8, 7)),
        Item(2, 'Carrot Soap', 3.49, 40, 8, datetime.date(2023, 8, 7)),
        Item(3, 'Raspberry Soap', 3.49, 28, 20, datetime.date(2023, 8, 8)),
        Item(4, 'Apple Soap', 3.49, 28, 20, datetime.date(2023, 8, 7)),
        Item(5, 'Orange Soap', 3.49, 26, 22, datetime.date(2023, 8, 8)),
        Item(6, 'Banana Soap', 3.49, 42, 6, datetime.date(2023, 8, 7)),
        Item(7, 'Tea Soap', 3.49, 64, 32, datetime.date(2023, 8, 7)),
        Item(8, 'Coffee Soap', 3.49, 33, 15, datetime.date(2023, 8, 7)),
        Item(9, 'Peach Soap', 3.49, 16, 80, datetime.date(2023, 8, 8)),
        Item(10, 'Rose Soap', 3.49, 50, 46, datetime.date(2023, 8, 8))
    ]
    assert place_order(db_connection, "Alfred", [{"item_id": 6, "quantity": 1}, {"item_id": 7, "quantity": 1},
                                                {"item_id": 1, "quantity": 2}]) == "All items ordered successfully."
    assert order_repository.get_all('total_price', reverse=True) == [
        Order(11, 'Cathy', datetime.date(2023, 8, 7), 27.92),
        Order(16, 'Stacey', datetime.date(2023, 8, 7), 24.43),
        Order(14, 'Benson', datetime.date(2023, 8, 7), 20.94),
        Order(22, 'William', datetime.date(2023, 8, 8), 20.94),
        Order(15, 'Kevin', datetime.date(2023, 8, 7), 17.45),
        Order(6, 'Kate', datetime.date(2023, 8, 7), 13.96),
        Order(9, 'John', datetime.date(2023, 8, 7), 13.96),
        Order(12, 'Ann', datetime.date(2023, 8, 7), 13.96),
        Order(13, 'Scott', datetime.date(2023, 8, 7), 13.96),
        Order(23, 'Alfred', datetime.date(2023, 8, 8), 13.96),
        Order(10, 'Ricky', datetime.date(2023, 8, 7), 10.47),
        Order(19, 'Laura', datetime.date(2023, 8, 7), 10.47),
        Order(21, 'Owen', datetime.date(2023, 8, 8), 10.47),
        Order(4, 'Ben', datetime.date(2023, 8, 7), 6.98),
        Order(17, 'Tracey', datetime.date(2023, 8, 7), 6.98),
        Order(20, 'Kay', datetime.date(2023, 8, 7), 6.98),
        Order(1, 'Merry', datetime.date(2023, 8, 6), 3.49),
        Order(2, 'Andrew', datetime.date(2023, 8, 7), 3.49),
        Order(3, 'Alex', datetime.date(2023, 8, 7), 3.49),
        Order(5, 'Amy', datetime.date(2023, 8, 7), 3.49),
        Order(7, 'Rose', datetime.date(2023, 8, 7), 3.49),
        Order(8, 'Art', datetime.date(2023, 8, 7), 3.49),
        Order(18, 'Emma', datetime.date(2023, 8, 7), 3.49)
    ]
    assert item_repository.get_all("id") == [
        Item(1, 'Blueberry Soap', 3.49, 32, 16, datetime.date(2023, 8, 8)),
        Item(2, 'Carrot Soap', 3.49, 40, 8, datetime.date(2023, 8, 7)),
        Item(3, 'Raspberry Soap', 3.49, 28, 20, datetime.date(2023, 8, 8)),
        Item(4, 'Apple Soap', 3.49, 28, 20, datetime.date(2023, 8, 7)),
        Item(5, 'Orange Soap', 3.49, 26, 22, datetime.date(2023, 8, 8)),
        Item(6, 'Banana Soap', 3.49, 41, 7, datetime.date(2023, 8, 8)),
        Item(7, 'Tea Soap', 3.49, 63, 33, datetime.date(2023, 8, 8)),
        Item(8, 'Coffee Soap', 3.49, 33, 15, datetime.date(2023, 8, 7)),
        Item(9, 'Peach Soap', 3.49, 16, 80, datetime.date(2023, 8, 8)),
        Item(10, 'Rose Soap', 3.49, 50, 46, datetime.date(2023, 8, 8))
    ]
    assert place_order(db_connection, "Joseph", [{"item_id": 9, "quantity": 17},
                                                {"item_id": 3, "quantity": 5}]) == "Insufficient stock for some of the items you ordered.\nAvailable items were ordered. Check your order details.\nYou may try ordering a fewer amount of the unsuccessful items."
    assert item_repository.get_all("id") == [
        Item(1, 'Blueberry Soap', 3.49, 32, 16, datetime.date(2023, 8, 8)),
        Item(2, 'Carrot Soap', 3.49, 40, 8, datetime.date(2023, 8, 7)),
        Item(3, 'Raspberry Soap', 3.49, 23, 25, datetime.date(2023, 8, 8)),
        Item(4, 'Apple Soap', 3.49, 28, 20, datetime.date(2023, 8, 7)),
        Item(5, 'Orange Soap', 3.49, 26, 22, datetime.date(2023, 8, 8)),
        Item(6, 'Banana Soap', 3.49, 41, 7, datetime.date(2023, 8, 8)),
        Item(7, 'Tea Soap', 3.49, 63, 33, datetime.date(2023, 8, 8)),
        Item(8, 'Coffee Soap', 3.49, 33, 15, datetime.date(2023, 8, 7)),
        Item(9, 'Peach Soap', 3.49, 16, 80, datetime.date(2023, 8, 8)),
        Item(10, 'Rose Soap', 3.49, 50, 46, datetime.date(2023, 8, 8))
    ]
    assert place_order(db_connection, "Wendy", [{"item_id": 4, "quantity": 50},
                                                {"item_id": 10, "quantity": 70}]) == "Insufficient stock. Your order was not placed."

def test_get_partial_refund(db_connection):
    db_connection.seed('seeds/items_orders.sql')
    order_repository = OrderRepository(db_connection)
    item_repository = ItemRepository(db_connection)
    assert get_partial_refund(db_connection, 14, [{"item_id": 3, "quantity": 1},
                                                {"item_id": 5, "quantity": 1}]) == "Your selected items have been refunded."
    assert order_repository.find_by_id_and_show_item_details(14) == [
        ItemInOrder(2, "Carrot Soap", 2, 6.98),
        ItemInOrder(5, "Orange Soap", 1, 3.49),
        ItemInOrder(7, "Tea Soap", 1, 3.49)
    ]
    assert item_repository.get_all("id") == [
        Item(1, 'Blueberry Soap', 3.49, 34, 14, datetime.date(2023, 8, 7)),
        Item(2, 'Carrot Soap', 3.49, 40, 8, datetime.date(2023, 8, 7)),
        Item(3, 'Raspberry Soap', 3.49, 32, 16, datetime.date(2023, 8, 8)),
        Item(4, 'Apple Soap', 3.49, 28, 20, datetime.date(2023, 8, 7)),
        Item(5, 'Orange Soap', 3.49, 28, 20, datetime.date(2023, 8, 7)),
        Item(6, 'Banana Soap', 3.49, 42, 6, datetime.date(2023, 8, 7)),
        Item(7, 'Tea Soap', 3.49, 64, 32, datetime.date(2023, 8, 7)),
        Item(8, 'Coffee Soap', 3.49, 33, 15, datetime.date(2023, 8, 7)),
        Item(9, 'Peach Soap', 3.49, 18, 78, datetime.date(2023, 8, 7)),
        Item(10, 'Rose Soap', 3.49, 50, 46, datetime.date(2023, 8, 8))
    ]
    assert get_partial_refund(db_connection, 14, [{"item_id": 2, "quantity": 2}, {"item_id": 5, "quantity": 1},
                                                {"item_id": 7, "quantity": 1}]) == "Your order has been cancelled and refunded."
    assert order_repository.get_all('id') == [
        Order(1, 'Merry', datetime.date(2023, 8, 6), 3.49),
        Order(2, 'Andrew', datetime.date(2023, 8, 7), 3.49),
        Order(3, 'Alex', datetime.date(2023, 8, 7), 3.49),
        Order(4, 'Ben', datetime.date(2023, 8, 7), 6.98),
        Order(5, 'Amy', datetime.date(2023, 8, 7), 3.49),
        Order(6, 'Kate', datetime.date(2023, 8, 7), 13.96),
        Order(7, 'Rose', datetime.date(2023, 8, 7), 3.49),
        Order(8, 'Art', datetime.date(2023, 8, 7), 3.49),
        Order(9, 'John', datetime.date(2023, 8, 7), 13.96),
        Order(10, 'Ricky', datetime.date(2023, 8, 7), 10.47),
        Order(11, 'Cathy', datetime.date(2023, 8, 7), 27.92),
        Order(12, 'Ann', datetime.date(2023, 8, 7), 13.96),
        Order(13, 'Scott', datetime.date(2023, 8, 7), 13.96),
        Order(15, 'Kevin', datetime.date(2023, 8, 7), 17.45),
        Order(16, 'Stacey', datetime.date(2023, 8, 7), 24.43),
        Order(17, 'Tracey', datetime.date(2023, 8, 7), 6.98),
        Order(18, 'Emma', datetime.date(2023, 8, 7), 3.49), 
        Order(19, 'Laura', datetime.date(2023, 8, 7), 10.47),
        Order(20, 'Kay', datetime.date(2023, 8, 7), 6.98),
        Order(21, 'Owen', datetime.date(2023, 8, 8), 10.47)
    ]
    assert get_partial_refund(db_connection, 21, [{"item_id": 3, "quantity": 1}]) == "Your selected items have been refunded."
    assert item_repository.get_all("id") == [
        Item(1, 'Blueberry Soap', 3.49, 34, 14, datetime.date(2023, 8, 7)),
        Item(2, 'Carrot Soap', 3.49, 42, 6, datetime.date(2023, 8, 7)),
        Item(3, 'Raspberry Soap', 3.49, 33, 15, datetime.date(2023, 8, 7)),
        Item(4, 'Apple Soap', 3.49, 28, 20, datetime.date(2023, 8, 7)),
        Item(5, 'Orange Soap', 3.49, 29, 19, datetime.date(2023, 8, 7)),
        Item(6, 'Banana Soap', 3.49, 42, 6, datetime.date(2023, 8, 7)),
        Item(7, 'Tea Soap', 3.49, 65, 31, datetime.date(2023, 8, 7)),
        Item(8, 'Coffee Soap', 3.49, 33, 15, datetime.date(2023, 8, 7)),
        Item(9, 'Peach Soap', 3.49, 18, 78, datetime.date(2023, 8, 7)),
        Item(10, 'Rose Soap', 3.49, 50, 46, datetime.date(2023, 8, 8))
    ]

def test_get_full_refund(db_connection):
    db_connection.seed('seeds/items_orders.sql')
    item_repository = ItemRepository(db_connection)
    order_repository = OrderRepository(db_connection)
    assert get_full_refund(db_connection, 6) == "Your order has been cancelled and refunded."
    assert order_repository.get_all('id') == [
        Order(1, 'Merry', datetime.date(2023, 8, 6), 3.49),
        Order(2, 'Andrew', datetime.date(2023, 8, 7), 3.49),
        Order(3, 'Alex', datetime.date(2023, 8, 7), 3.49),
        Order(4, 'Ben', datetime.date(2023, 8, 7), 6.98),
        Order(5, 'Amy', datetime.date(2023, 8, 7), 3.49),
        Order(7, 'Rose', datetime.date(2023, 8, 7), 3.49),
        Order(8, 'Art', datetime.date(2023, 8, 7), 3.49),
        Order(9, 'John', datetime.date(2023, 8, 7), 13.96),
        Order(10, 'Ricky', datetime.date(2023, 8, 7), 10.47),
        Order(11, 'Cathy', datetime.date(2023, 8, 7), 27.92),
        Order(12, 'Ann', datetime.date(2023, 8, 7), 13.96),
        Order(13, 'Scott', datetime.date(2023, 8, 7), 13.96),
        Order(14, 'Benson', datetime.date(2023, 8, 7), 20.94),
        Order(15, 'Kevin', datetime.date(2023, 8, 7), 17.45),
        Order(16, 'Stacey', datetime.date(2023, 8, 7), 24.43),
        Order(17, 'Tracey', datetime.date(2023, 8, 7), 6.98),
        Order(18, 'Emma', datetime.date(2023, 8, 7), 3.49), 
        Order(19, 'Laura', datetime.date(2023, 8, 7), 10.47),
        Order(20, 'Kay', datetime.date(2023, 8, 7), 6.98),
        Order(21, 'Owen', datetime.date(2023, 8, 8), 10.47)
    ]
    assert item_repository.get_all("id") == [
        Item(1, 'Blueberry Soap', 3.49, 34, 14, datetime.date(2023, 8, 7)),
        Item(2, 'Carrot Soap', 3.49, 41, 7, datetime.date(2023, 8, 7)),
        Item(3, 'Raspberry Soap', 3.49, 31, 17, datetime.date(2023, 8, 8)),
        Item(4, 'Apple Soap', 3.49, 28, 20, datetime.date(2023, 8, 7)),
        Item(5, 'Orange Soap', 3.49, 27, 21, datetime.date(2023, 8, 7)),
        Item(6, 'Banana Soap', 3.49, 45, 3, datetime.date(2023, 8, 7)),
        Item(7, 'Tea Soap', 3.49, 64, 32, datetime.date(2023, 8, 7)),
        Item(8, 'Coffee Soap', 3.49, 33, 15, datetime.date(2023, 8, 7)),
        Item(9, 'Peach Soap', 3.49, 18, 78, datetime.date(2023, 8, 7)),
        Item(10, 'Rose Soap', 3.49, 50, 46, datetime.date(2023, 8, 8))
    ]
