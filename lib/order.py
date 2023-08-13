class Order:

    def __init__(self, id, customer_name, date, total_price):
        self.id = id
        self.customer_name = customer_name
        self.date = date
        self.total_price = total_price

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
