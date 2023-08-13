class ItemInOrder:

    def __init__(self, id, name, quantity, price):
        self.id = id
        self.name = name
        self.quantity = quantity
        self.price = price
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__
