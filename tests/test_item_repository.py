from lib.item import *
from lib.item_repository import *
from lib.order_in_item import *
import datetime

def test_get_all_items(db_connection):
    db_connection.seed('seeds/items_orders.sql')
    item_repository = ItemRepository(db_connection)
    assert item_repository.get_all("id") == [
        Item(1, 'Blueberry Soap', 3.49, 34, 14, datetime.date(2023, 8, 7)),
        Item(2, 'Carrot Soap', 3.49, 40, 8, datetime.date(2023, 8, 7)),
        Item(3, 'Raspberry Soap', 3.49, 31, 17, datetime.date(2023, 8, 8)),
        Item(4, 'Apple Soap', 3.49, 28, 20, datetime.date(2023, 8, 7)),
        Item(5, 'Orange Soap', 3.49, 27, 21, datetime.date(2023, 8, 7)),
        Item(6, 'Banana Soap', 3.49, 42, 6, datetime.date(2023, 8, 7)),
        Item(7, 'Tea Soap', 3.49, 64, 32, datetime.date(2023, 8, 7)),
        Item(8, 'Coffee Soap', 3.49, 33, 15, datetime.date(2023, 8, 7)),
        Item(9, 'Peach Soap', 3.49, 18, 78, datetime.date(2023, 8, 7)),
        Item(10, 'Rose Soap', 3.49, 50, 46, datetime.date(2023, 8, 8))
    ]
    assert item_repository.get_all("price") == [
        Item(1, 'Blueberry Soap', 3.49, 34, 14, datetime.date(2023, 8, 7)),
        Item(2, 'Carrot Soap', 3.49, 40, 8, datetime.date(2023, 8, 7)),
        Item(3, 'Raspberry Soap', 3.49, 31, 17, datetime.date(2023, 8, 8)),
        Item(4, 'Apple Soap', 3.49, 28, 20, datetime.date(2023, 8, 7)),
        Item(5, 'Orange Soap', 3.49, 27, 21, datetime.date(2023, 8, 7)),
        Item(6, 'Banana Soap', 3.49, 42, 6, datetime.date(2023, 8, 7)),
        Item(7, 'Tea Soap', 3.49, 64, 32, datetime.date(2023, 8, 7)),
        Item(8, 'Coffee Soap', 3.49, 33, 15, datetime.date(2023, 8, 7)),
        Item(9, 'Peach Soap', 3.49, 18, 78, datetime.date(2023, 8, 7)),
        Item(10, 'Rose Soap', 3.49, 50, 46, datetime.date(2023, 8, 8))
    ]
    assert item_repository.get_all("stock", reverse=True) == [
        Item(7, 'Tea Soap', 3.49, 64, 32, datetime.date(2023, 8, 7)),
        Item(10, 'Rose Soap', 3.49, 50, 46, datetime.date(2023, 8, 8)),
        Item(6, 'Banana Soap', 3.49, 42, 6, datetime.date(2023, 8, 7)),
        Item(2, 'Carrot Soap', 3.49, 40, 8, datetime.date(2023, 8, 7)),
        Item(1, 'Blueberry Soap', 3.49, 34, 14, datetime.date(2023, 8, 7)),
        Item(8, 'Coffee Soap', 3.49, 33, 15, datetime.date(2023, 8, 7)),
        Item(3, 'Raspberry Soap', 3.49, 31, 17, datetime.date(2023, 8, 8)),
        Item(4, 'Apple Soap', 3.49, 28, 20, datetime.date(2023, 8, 7)),
        Item(5, 'Orange Soap', 3.49, 27, 21, datetime.date(2023, 8, 7)),
        Item(9, 'Peach Soap', 3.49, 18, 78, datetime.date(2023, 8, 7))
    ]
    assert item_repository.get_all("amount_sold") == [
        Item(6, 'Banana Soap', 3.49, 42, 6, datetime.date(2023, 8, 7)),
        Item(2, 'Carrot Soap', 3.49, 40, 8, datetime.date(2023, 8, 7)),
        Item(1, 'Blueberry Soap', 3.49, 34, 14, datetime.date(2023, 8, 7)),
        Item(8, 'Coffee Soap', 3.49, 33, 15, datetime.date(2023, 8, 7)),
        Item(3, 'Raspberry Soap', 3.49, 31, 17, datetime.date(2023, 8, 8)),
        Item(4, 'Apple Soap', 3.49, 28, 20, datetime.date(2023, 8, 7)),
        Item(5, 'Orange Soap', 3.49, 27, 21, datetime.date(2023, 8, 7)),
        Item(7, 'Tea Soap', 3.49, 64, 32, datetime.date(2023, 8, 7)),
        Item(10, 'Rose Soap', 3.49, 50, 46, datetime.date(2023, 8, 8)),
        Item(9, 'Peach Soap', 3.49, 18, 78, datetime.date(2023, 8, 7))
    ]
    assert item_repository.get_all("name") == [
        Item(4, 'Apple Soap', 3.49, 28, 20, datetime.date(2023, 8, 7)),
        Item(6, 'Banana Soap', 3.49, 42, 6, datetime.date(2023, 8, 7)),
        Item(1, 'Blueberry Soap', 3.49, 34, 14, datetime.date(2023, 8, 7)),
        Item(2, 'Carrot Soap', 3.49, 40, 8, datetime.date(2023, 8, 7)),
        Item(8, 'Coffee Soap', 3.49, 33, 15, datetime.date(2023, 8, 7)),
        Item(5, 'Orange Soap', 3.49, 27, 21, datetime.date(2023, 8, 7)),
        Item(9, 'Peach Soap', 3.49, 18, 78, datetime.date(2023, 8, 7)),
        Item(3, 'Raspberry Soap', 3.49, 31, 17, datetime.date(2023, 8, 8)),
        Item(10, 'Rose Soap', 3.49, 50, 46, datetime.date(2023, 8, 8)),
        Item(7, 'Tea Soap', 3.49, 64, 32, datetime.date(2023, 8, 7))
    ]
    assert item_repository.get_all("last_date_sold", reverse=True) == [
        Item(3, 'Raspberry Soap', 3.49, 31, 17, datetime.date(2023, 8, 8)),
        Item(10, 'Rose Soap', 3.49, 50, 46, datetime.date(2023, 8, 8)),
        Item(1, 'Blueberry Soap', 3.49, 34, 14, datetime.date(2023, 8, 7)),
        Item(2, 'Carrot Soap', 3.49, 40, 8, datetime.date(2023, 8, 7)),
        Item(4, 'Apple Soap', 3.49, 28, 20, datetime.date(2023, 8, 7)),
        Item(5, 'Orange Soap', 3.49, 27, 21, datetime.date(2023, 8, 7)),
        Item(6, 'Banana Soap', 3.49, 42, 6, datetime.date(2023, 8, 7)),
        Item(7, 'Tea Soap', 3.49, 64, 32, datetime.date(2023, 8, 7)),
        Item(8, 'Coffee Soap', 3.49, 33, 15, datetime.date(2023, 8, 7)),
        Item(9, 'Peach Soap', 3.49, 18, 78, datetime.date(2023, 8, 7))
    ]

def test_find_by_id(db_connection):
    db_connection.seed('seeds/items_orders.sql')
    item_repository = ItemRepository(db_connection)
    assert item_repository.find_by_id(4) == Item(4, 'Apple Soap', 3.49, 28, 20, datetime.date(2023, 8, 7))

def test_find_by_name(db_connection):
    db_connection.seed('seeds/items_orders.sql')
    item_repository = ItemRepository(db_connection)
    assert item_repository.find_by_name("berry") == [
        Item(1, 'Blueberry Soap', 3.49, 34, 14, datetime.date(2023, 8, 7)),
        Item(3, 'Raspberry Soap', 3.49, 31, 17, datetime.date(2023, 8, 8))
    ]
    assert item_repository.find_by_name("orange") == [
        Item(5, 'Orange Soap', 3.49, 27, 21, datetime.date(2023, 8, 7))
    ]
    assert item_repository.find_by_name("grape") == []
    assert item_repository.find_by_name("soap") == [
        Item(1, 'Blueberry Soap', 3.49, 34, 14, datetime.date(2023, 8, 7)),
        Item(2, 'Carrot Soap', 3.49, 40, 8, datetime.date(2023, 8, 7)),
        Item(3, 'Raspberry Soap', 3.49, 31, 17, datetime.date(2023, 8, 8)),
        Item(4, 'Apple Soap', 3.49, 28, 20, datetime.date(2023, 8, 7)),
        Item(5, 'Orange Soap', 3.49, 27, 21, datetime.date(2023, 8, 7)),
        Item(6, 'Banana Soap', 3.49, 42, 6, datetime.date(2023, 8, 7)),
        Item(7, 'Tea Soap', 3.49, 64, 32, datetime.date(2023, 8, 7)),
        Item(8, 'Coffee Soap', 3.49, 33, 15, datetime.date(2023, 8, 7)),
        Item(9, 'Peach Soap', 3.49, 18, 78, datetime.date(2023, 8, 7)),
        Item(10, 'Rose Soap', 3.49, 50, 46, datetime.date(2023, 8, 8))
    ]

def test_find_by_id_and_show_order_details(db_connection):
    db_connection.seed('seeds/items_orders.sql')
    item_repository = ItemRepository(db_connection)
    assert item_repository.find_by_id_and_show_order_details(10) == [
        OrderInItem(10, 'Ricky', 2, datetime.date(2023, 8, 7)),
        OrderInItem(13, 'Scott', 1, datetime.date(2023, 8, 7)),
        OrderInItem(15, 'Kevin', 4, datetime.date(2023, 8, 7)),
        OrderInItem(21, 'Owen', 2, datetime.date(2023, 8, 8))
    ]

def test_add_item(db_connection):
    db_connection.seed('seeds/items_orders.sql')
    item_repository = ItemRepository(db_connection)
    item_repository.add_item("Peanut Soap", "3.99", 48)
    assert item_repository.get_all("id") == [
        Item(1, 'Blueberry Soap', 3.49, 34, 14, datetime.date(2023, 8, 7)),
        Item(2, 'Carrot Soap', 3.49, 40, 8, datetime.date(2023, 8, 7)),
        Item(3, 'Raspberry Soap', 3.49, 31, 17, datetime.date(2023, 8, 8)),
        Item(4, 'Apple Soap', 3.49, 28, 20, datetime.date(2023, 8, 7)),
        Item(5, 'Orange Soap', 3.49, 27, 21, datetime.date(2023, 8, 7)),
        Item(6, 'Banana Soap', 3.49, 42, 6, datetime.date(2023, 8, 7)),
        Item(7, 'Tea Soap', 3.49, 64, 32, datetime.date(2023, 8, 7)),
        Item(8, 'Coffee Soap', 3.49, 33, 15, datetime.date(2023, 8, 7)),
        Item(9, 'Peach Soap', 3.49, 18, 78, datetime.date(2023, 8, 7)),
        Item(10, 'Rose Soap', 3.49, 50, 46, datetime.date(2023, 8, 8)),
        Item(11, 'Peanut Soap', 3.99, 48, 0, datetime.date(1, 1, 1))
    ]
    assert item_repository.get_all("last_date_sold", reverse=True) == [
        Item(3, 'Raspberry Soap', 3.49, 31, 17, datetime.date(2023, 8, 8)),
        Item(10, 'Rose Soap', 3.49, 50, 46, datetime.date(2023, 8, 8)),
        Item(1, 'Blueberry Soap', 3.49, 34, 14, datetime.date(2023, 8, 7)),
        Item(2, 'Carrot Soap', 3.49, 40, 8, datetime.date(2023, 8, 7)),
        Item(4, 'Apple Soap', 3.49, 28, 20, datetime.date(2023, 8, 7)),
        Item(5, 'Orange Soap', 3.49, 27, 21, datetime.date(2023, 8, 7)),
        Item(6, 'Banana Soap', 3.49, 42, 6, datetime.date(2023, 8, 7)),
        Item(7, 'Tea Soap', 3.49, 64, 32, datetime.date(2023, 8, 7)),
        Item(8, 'Coffee Soap', 3.49, 33, 15, datetime.date(2023, 8, 7)),
        Item(9, 'Peach Soap', 3.49, 18, 78, datetime.date(2023, 8, 7)),
        Item(11, 'Peanut Soap', 3.99, 48, 0, datetime.date(1, 1, 1))
    ]

def test_update_item(db_connection):
    db_connection.seed('seeds/items_orders.sql')
    item_repository = ItemRepository(db_connection)
    item_repository.update_item(7, price=4.49)
    assert item_repository.find_by_id(7) == Item(7, 'Tea Soap', 4.49, 64, 32, datetime.date(2023, 8, 7))
    assert item_repository.update_item(6, adjust_stock=-2, add_amount_sold=2) == None
    assert item_repository.find_by_id(6) == Item(6, 'Banana Soap', 3.49, 40, 8, datetime.date(2023, 8, 7))
    assert item_repository.update_item(9, adjust_stock=-18, add_amount_sold=18) == None
    assert item_repository.find_by_id(9) == Item(9, 'Peach Soap', 3.49, 0, 96, datetime.date(2023, 8, 7))
    assert item_repository.update_item(4, adjust_stock=-29, add_amount_sold=29) == False
    assert item_repository.find_by_id(4) == Item(4, 'Apple Soap', 3.49, 28, 20, datetime.date(2023, 8, 7))

def test_delete_item(db_connection):
    db_connection.seed('seeds/items_orders.sql')
    item_repository = ItemRepository(db_connection)
    assert item_repository.delete_item(4) == False
    assert item_repository.find_by_id(4) == Item(4, 'Apple Soap', 3.49, 28, 20, datetime.date(2023, 8, 7))
    item_repository.add_item("Peanut Soap", "3.99", 48)
    assert item_repository.find_by_id(11) == Item(11, 'Peanut Soap', 3.99, 48, 0, datetime.date(1, 1, 1))
    assert item_repository.delete_item(11) == None
    assert item_repository.get_all("id") == [
        Item(1, 'Blueberry Soap', 3.49, 34, 14, datetime.date(2023, 8, 7)),
        Item(2, 'Carrot Soap', 3.49, 40, 8, datetime.date(2023, 8, 7)),
        Item(3, 'Raspberry Soap', 3.49, 31, 17, datetime.date(2023, 8, 8)),
        Item(4, 'Apple Soap', 3.49, 28, 20, datetime.date(2023, 8, 7)),
        Item(5, 'Orange Soap', 3.49, 27, 21, datetime.date(2023, 8, 7)),
        Item(6, 'Banana Soap', 3.49, 42, 6, datetime.date(2023, 8, 7)),
        Item(7, 'Tea Soap', 3.49, 64, 32, datetime.date(2023, 8, 7)),
        Item(8, 'Coffee Soap', 3.49, 33, 15, datetime.date(2023, 8, 7)),
        Item(9, 'Peach Soap', 3.49, 18, 78, datetime.date(2023, 8, 7)),
        Item(10, 'Rose Soap', 3.49, 50, 46, datetime.date(2023, 8, 8))
    ]
    