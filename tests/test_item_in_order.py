from lib.item_in_order import *

def test_item_in_order_constructs():
    item_in_order = ItemInOrder(5, "Blackberry Juice", 2, 8.50)
    assert item_in_order.id == 5
    assert item_in_order.name ==  "Blackberry Juice"
    assert item_in_order.quantity == 2
    assert item_in_order.price == 8.50

def test_item_in_order_instances_are_equal():
    item_in_order1 = ItemInOrder(5, "Blackberry Juice", 2, 7.80)
    item_in_order2 = ItemInOrder(5, "Blackberry Juice", 2, 7.80)
    assert item_in_order1 == item_in_order2
