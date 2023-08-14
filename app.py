from lib.database_connection import DatabaseConnection
from lib.item_repository import *
from lib.order_repository import *
from lib.calling_both_repositories import *

class Application():
    def __init__(self):
        self._connection = DatabaseConnection()
        self._connection.connect()
        self._connection.seed("seeds/items_orders.sql")
    
    def is_float(self, string):
        try:
            float(string)
            return True
        except ValueError:
            return False

    def f_number(self, number):
        number = str(number)
        if "." not in number:
            return number + ".00"
        else:
            if len(number.rsplit('.')[1]) == 1:
                return number + "0"
            else:
                return number

    def print_all_items(self, all_items):
        print("")
        for item in all_items:
            print(f"Item ID: {item.id}   {item.name}   £{self.f_number(item.price)}   Stock: {item.stock}   Sold: {item.amount_sold}   Last Date Sold: {item.last_date_sold}")

    def see_all_items(self):
        item_repository = ItemRepository(self._connection)
        all_items = item_repository.get_all('id')
        self.print_all_items(all_items)
        while True:
            print("\nI = Sort by item ID."
                "               ABC = Sort alphabetically."
                "\nL = Sort by price (low to high)."
                "     H = Sort by price (high to low)."
                "\nS = Sort by stock (low to high)."
                "     C = Sort by stock (high to low)."
                "\nP = Sort by sales (high to low)."
                "     N = Sort by sales (low to high)."
                "\nD = Sort by last date sold."
                "          F = Sort by last date sold - least recent."
                "\nType in the item ID and press Enter to see all the orders this item appears in."
                "\nA = Add new item."
                "\nItem ID + S to update item stock."
                "    Item ID + P to update item price."
                "\nB = Back to main menu.")
            choice = input("\nPick an option: ")
            choice = choice.lower()
            if choice == "b":
                break
            elif choice == "i":
                self.print_all_items(item_repository.get_all('id'))
            elif choice == "abc":
                self.print_all_items(item_repository.get_all('name'))
            elif choice  == "l":
                self.print_all_items(item_repository.get_all('price'))
            elif choice == "h":
                self.print_all_items(item_repository.get_all('price', reverse=True))
            elif choice == "s":
                self.print_all_items(item_repository.get_all('stock'))
            elif choice == "c":
                self.print_all_items(item_repository.get_all('stock', reverse=True))
            elif choice == "p":
                self.print_all_items(item_repository.get_all('amount_sold', reverse=True))
            elif choice == "n":
                self.print_all_items(item_repository.get_all('amount_sold'))
            elif choice == "d":
                self.print_all_items(item_repository.get_all('last_date_sold', reverse=True))
            elif choice == "f":
                self.print_all_items(item_repository.get_all('last_date_sold'))
            elif len(choice) > 1 and choice[-1] == "s" and choice[:-1].isnumeric() and choice[:-1] != "0":
                self.update_item_stock(int(choice[:-1]))
            elif len(choice) > 1 and choice[-1] == "p" and choice[:-1].isnumeric() and choice[:-1] != "0":
                self.update_item_price(int(choice[:-1]))
            else:
                print("\nUnrecognised command!")

    def update_item_price(self, choice):
        item_repository = ItemRepository(self._connection)
        show_item = self.find_item_by_id(choice)
        if show_item == False:
            return False
        while True:
            new_item_price = input("\nEnter the new price for this item: £")
            if self.is_float(new_item_price) and len(new_item_price.rsplit(".")[-1]) <= 2:
                break
            print("\nUnrecognised price!")
        item_repository.update_item(choice, price=float(new_item_price))
        print("\nPrice updated. Check amended details below.")
        show_item = self.find_item_by_id(choice)
        input("\nPress Enter to continue.")
        
    def update_item_stock(self, choice):
        item_repository = ItemRepository(self._connection)
        show_item = self.find_item_by_id(choice)
        if show_item == False:
            return False
        while True:
            stock_adjustment = input("\nEnter amount to add or subtract from stock: ")
            if stock_adjustment.isnumeric() or (stock_adjustment[1:].isnumeric() and stock_adjustment[0] == "-"):
                break
            print("\nUnrecognised input!")
        item_repository.update_item(choice, adjust_stock=int(stock_adjustment))
        print("\nStock updated. Check amended details below.")
        show_item = self.find_item_by_id(choice)
        input("\nPress Enter to continue.")

    def find_item_by_id(self, id=0):
        item_repository = ItemRepository(self._connection)
        while id == 0:
            item_id = input("\nEnter item ID: ")
            if item_id.isnumeric() and item_id != "0":
                item_id = int(item_id)
                id = item_id
        found_item = item_repository.find_by_id(id)
        if not isinstance(found_item, Item):
            print("\nItem ID does not exist. Item could not be found.")
            return False
        self.print_all_items([found_item])

    def find_item_by_name(self):
        item_repository = ItemRepository(self._connection)
        search = input("\nEnter item name or part of name: ")
        


    def show_order_details_for_item(self):
        pass

    def add_new_item(self):
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
        print("\nWelcome to your supreme data program!")
        while True:
            print("\n\nWhat would you like to do?"
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
            elif choice == "1":
                self.see_all_items()
            elif choice == "2":
                self.find_item_by_id()
                print("\nPress Enter to continue.")
            elif choice == "3":
                self.find_item_by_name()
            elif choice == "4":
                self.delete_unused_item()
            elif choice == "5":
                self.see_all_orders()
            elif choice == "6":
                self.find_order_by_id()
            elif choice == "7":
                self.find_order_by_customer_name()
            elif choice == "8":
                self.place_order()
            elif choice == "9":
                self.get_refund()
            else:
                print("Invalid command!")
        

if __name__ == '__main__':
    app = Application()
    app.run()
