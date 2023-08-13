class OrderInItem:

    def __init__(self, id, customer_name, quantity, date):
        self.id = id
        self.customer_name = customer_name
        self.quantity = quantity
        self.date = date

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
