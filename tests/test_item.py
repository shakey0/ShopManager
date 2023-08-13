from lib.item import *

def test_item_constructs():
    item = Item(44, "Raspberry Body Wash", 3.49, 34, 14, "2023/8/5")
    assert item.id == 44
    assert item.name == "Raspberry Body Wash"
    assert item.price == 3.49
    assert item.stock == 34
    assert item.amount_sold == 14
    assert item.last_date_sold == "2023/8/5"

def test_item_instances_are_equal():
    item1 = Item(44, "Caramel Body Wash", 3.49, 34, 14, "2023/8/5")
    item2 = Item(44, "Caramel Body Wash", 3.49, 34, 14, "2023/8/5")
    assert item1 == item2