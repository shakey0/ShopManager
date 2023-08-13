from lib.order_in_item import *

def test_order_in_item_constructs():
    order_in_item = OrderInItem(9, "Fred", 3, "2023/8/5")
    assert order_in_item.id == 9
    assert order_in_item.customer_name == "Fred"
    assert order_in_item.quantity == 3
    assert order_in_item.date == "2023/8/5"

def test_order_in_item_instances_are_equal():
    order_in_item1 = OrderInItem(9, "Fred", 3, "2023/8/5")
    order_in_item2 = OrderInItem(9, "Fred", 3, "2023/8/5")
    assert order_in_item1 == order_in_item2
