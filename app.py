from lib.database_connection import DatabaseConnection
from lib.item_repository import *
from lib.order_repository import *
from lib.calling_both_repositories import *

class Application():
    def __init__(self):
        self._connection = DatabaseConnection()
        self._connection.connect()
        self._connection.seed("seeds/music_library.sql")
                
    def see_all_items(self):
        item_repository = ItemRepository(self._connection)
        all_items = item_repository.get_all('id')
        for item in all_items:
            print(f"Item ID: {item.id}   {item.name}   £{item.price}   Stock: {item.stock}   Sold: {item.amount_sold}   Last Date Sold: {item.last_date_sold}")
        while True:
            print("\nABC = Sort alphabetically."
                "\nL = Sort by price (low to high)."
                "\nH = Sort by price (high to low)."
                "\nS = Sort by stock (low to high)."
                "\nC = Sort by stock (high to low)."
                "\nP = Sort by amount sold (high to low)."
                "\nN = Sort by amount sold (low to high)."
                "\nD = Sort by last date sold."
                "\nType in the item ID and press Enter for orders with item."
                "\nA = Add new item."
                "\nItem ID + S to update item stock."
                "\nItem ID + P to update item price.")
            choice = input("\nPick an option: ")
            choice = choice.lower()
            pass_command = {}

    def find_item_by_id(self):
        pass

    def find_item_by_name(self):
        pass

    def show_order_details_for_item(self):
        pass

    def add_new_item(self):
        pass

    def update_item_price(self):
        pass
    
    def update_item_stock(self):
        pass

    def delete_unused_item(self):
        pass

    def see_all_orders(self):
        pass

    def find_order_by_id(self):
        pass

    def find_order_by_customer_name(self):
        pass

    def show_item_details_in_order(self):
        pass

    def place_order(self):
        pass

    def get_refund(self):
        pass
    
    def run(self):
        while True:
            print("\nWelcome to your supreme data program!"
                "\n\nWhat would you like to do?"
                "\n1. See all items."
                "\n2. Find an item by its ID."
                "\n3. Find an item by its name."
                "\n4. Delete an unused item."
                "\n5. See all orders."
                "\n6. Find an order by its ID."
                "\n7. Find an order by customer name."
                "\n8. Place an order."
                "\n9. Get refund."
                "\nQ = Quit")
            choice = input("\nPick on option: ")
            if choice == 'Q' or choice == 'q':
                break
            pass_command = {"1": self.see_all_items(), "2": self.find_item_by_id(), "3": self.find_item_by_name(),
                            "4": self.delete_unused_item(), "5": self.see_all_orders(), "6": self.find_order_by_id(),
                            "7": self.find_order_by_customer_name(), "8": self.place_order(), "9": self.get_refund()}
            if choice in pass_command.keys():
                pass_command[choice]
            else:
                print("Invalid command!")
        

if __name__ == '__main__':
    app = Application()
    app.run()
