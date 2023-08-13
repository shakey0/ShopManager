class Item:

    def __init__(self, id, name, price, stock, amount_sold, last_date_sold):
        self.id = id
        self.name = name
        self.price = price
        self.stock = stock
        self.amount_sold = amount_sold
        self.last_date_sold = last_date_sold

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
