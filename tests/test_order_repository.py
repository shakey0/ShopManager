from lib.order import *
from lib.order_repository import *
from lib.item_in_order import *
import datetime

def test_get_all_orders(db_connection):
    db_connection.seed('seeds/items_orders.sql')
    order_repository = OrderRepository(db_connection)
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
        Order(14, 'Benson', datetime.date(2023, 8, 7), 20.94),
        Order(15, 'Kevin', datetime.date(2023, 8, 7), 17.45),
        Order(16, 'Stacey', datetime.date(2023, 8, 7), 24.43),
        Order(17, 'Tracey', datetime.date(2023, 8, 7), 6.98),
        Order(18, 'Emma', datetime.date(2023, 8, 7), 3.49), 
        Order(19, 'Laura', datetime.date(2023, 8, 7), 10.47),
        Order(20, 'Kay', datetime.date(2023, 8, 7), 6.98),
        Order(21, 'Owen', datetime.date(2023, 8, 8), 10.47)
    ]
    assert order_repository.get_all('customer_name') == [
        Order(3, 'Alex', datetime.date(2023, 8, 7), 3.49),
        Order(5, 'Amy', datetime.date(2023, 8, 7), 3.49),
        Order(2, 'Andrew', datetime.date(2023, 8, 7), 3.49),
        Order(12, 'Ann', datetime.date(2023, 8, 7), 13.96),
        Order(8, 'Art', datetime.date(2023, 8, 7), 3.49),
        Order(4, 'Ben', datetime.date(2023, 8, 7), 6.98),
        Order(14, 'Benson', datetime.date(2023, 8, 7), 20.94),
        Order(11, 'Cathy', datetime.date(2023, 8, 7), 27.92),
        Order(18, 'Emma', datetime.date(2023, 8, 7), 3.49), 
        Order(9, 'John', datetime.date(2023, 8, 7), 13.96),
        Order(6, 'Kate', datetime.date(2023, 8, 7), 13.96),
        Order(20, 'Kay', datetime.date(2023, 8, 7), 6.98),
        Order(15, 'Kevin', datetime.date(2023, 8, 7), 17.45),
        Order(19, 'Laura', datetime.date(2023, 8, 7), 10.47),
        Order(1, 'Merry', datetime.date(2023, 8, 6), 3.49),
        Order(21, 'Owen', datetime.date(2023, 8, 8), 10.47),
        Order(10, 'Ricky', datetime.date(2023, 8, 7), 10.47),
        Order(7, 'Rose', datetime.date(2023, 8, 7), 3.49),
        Order(13, 'Scott', datetime.date(2023, 8, 7), 13.96),
        Order(16, 'Stacey', datetime.date(2023, 8, 7), 24.43),
        Order(17, 'Tracey', datetime.date(2023, 8, 7), 6.98)
    ]
    assert order_repository.get_all('date', reverse=True) == [
        Order(21, 'Owen', datetime.date(2023, 8, 8), 10.47),
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
        Order(14, 'Benson', datetime.date(2023, 8, 7), 20.94),
        Order(15, 'Kevin', datetime.date(2023, 8, 7), 17.45),
        Order(16, 'Stacey', datetime.date(2023, 8, 7), 24.43),
        Order(17, 'Tracey', datetime.date(2023, 8, 7), 6.98),
        Order(18, 'Emma', datetime.date(2023, 8, 7), 3.49), 
        Order(19, 'Laura', datetime.date(2023, 8, 7), 10.47),
        Order(20, 'Kay', datetime.date(2023, 8, 7), 6.98),
        Order(1, 'Merry', datetime.date(2023, 8, 6), 3.49)
    ]
    assert order_repository.get_all('total_price', reverse=True) == [
        Order(11, 'Cathy', datetime.date(2023, 8, 7), 27.92),
        Order(16, 'Stacey', datetime.date(2023, 8, 7), 24.43),
        Order(14, 'Benson', datetime.date(2023, 8, 7), 20.94),
        Order(15, 'Kevin', datetime.date(2023, 8, 7), 17.45),
        Order(6, 'Kate', datetime.date(2023, 8, 7), 13.96),
        Order(9, 'John', datetime.date(2023, 8, 7), 13.96),
        Order(12, 'Ann', datetime.date(2023, 8, 7), 13.96),
        Order(13, 'Scott', datetime.date(2023, 8, 7), 13.96),
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

def test_find_id(db_connection):
    db_connection.seed('seeds/items_orders.sql')
    order_repository = OrderRepository(db_connection)
    assert order_repository.find_by_id(14) == Order(14, 'Benson', datetime.date(2023, 8, 7), 20.94)

def test_find_by_customer_name(db_connection):
    db_connection.seed('seeds/items_orders.sql')
    order_repository = OrderRepository(db_connection)
    assert order_repository.find_by_customer_name('john') == [
        Order(9, 'John', datetime.date(2023, 8, 7), 13.96)
    ]
    assert order_repository.find_by_customer_name('BEN') == [
        Order(4, 'Ben', datetime.date(2023, 8, 7), 6.98),
        Order(14, 'Benson', datetime.date(2023, 8, 7), 20.94)
    ]

def test_find_by_id_and_show_item_details(db_connection):
    db_connection.seed('seeds/items_orders.sql')
    order_repository = OrderRepository(db_connection)
    assert order_repository.find_by_id_and_show_item_details(14) == [
        ItemInOrder(2, "Carrot Soap", 2, 6.98),
        ItemInOrder(3, "Raspberry Soap", 1, 3.49),
        ItemInOrder(5, "Orange Soap", 2, 6.98),
        ItemInOrder(7, "Tea Soap", 1, 3.49)
    ]
    
def test_add_order(db_connection):
    db_connection.seed('seeds/items_orders.sql')
    order_repository = OrderRepository(db_connection)
    order_repository.add_order("William", [{"item_id": 3, "quantity": 3}, {"item_id": 5, "quantity": 1},
                                            {"item_id": 9, "quantity": 2}])
    assert order_repository.find_by_id(22) == Order(22, 'William', datetime.date(2023, 8, 8), 20.94)
    assert order_repository.find_by_id_and_show_item_details(22) == [
        ItemInOrder(3, "Raspberry Soap", 3, 10.47),
        ItemInOrder(5, "Orange Soap", 1, 3.49),
        ItemInOrder(9, "Peach Soap", 2, 6.98)
    ]
    order_repository.add_order("Alfred", [{"item_id": 6, "quantity": 1}, {"item_id": 7, "quantity": 1},
                                            {"item_id": 1, "quantity": 2}])
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

def test_remove_items_from_order(db_connection):
    db_connection.seed('seeds/items_orders.sql')
    order_repository = OrderRepository(db_connection)
    order_repository.remove_items_from_order(14, [{"item_id": 3, "quantity": 1},
                                                {"item_id": 5, "quantity": 1}])
    assert order_repository.find_by_id_and_show_item_details(14) == [
        ItemInOrder(2, "Carrot Soap", 2, 6.98),
        ItemInOrder(5, "Orange Soap", 1, 3.49),
        ItemInOrder(7, "Tea Soap", 1, 3.49)
    ]
    order_repository.remove_items_from_order(14, [{"item_id": 2, "quantity": 2}, {"item_id": 5, "quantity": 1},
                                                {"item_id": 7, "quantity": 1}])
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

def test_delete_order(db_connection):
    db_connection.seed('seeds/items_orders.sql')
    order_repository = OrderRepository(db_connection)
    order_repository.delete_order(6)
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
