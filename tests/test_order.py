from lib.order import *

def test_order_constructs():
    order = Order(105, "Andrew", "2023/8/4", 6.98)
    assert order.id == 105
    assert order.customer_name == "Andrew"
    assert order.date == "2023/8/4"
    assert order.total_price == 6.98

def test_order_instances_are_equal():
    order1 = Order(167, "Bobby", "2023/8/6", 6.98)
    order2 = Order(167, "Bobby", "2023/8/6", 6.98)
    assert order1 == order2